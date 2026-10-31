#!/usr/bin/env python3
"""Slušné stahování z archivů – ochrana před zablokováním (banem).

Použití (z kořene projektu):
  python3 -I scripts/slusne.py tools/<nastroj>.py [argumenty…]   – spustí Python nástroj s limity
  python3 -I scripts/slusne.py bash tools/<skript>.sh [argumenty…] – shellový skript (curl uvnitř dostane limity)
  python3 -I scripts/slusne.py curl [argumenty curl…]             – jednotlivé volání curl s limity

Pravidla (pro každý web zvlášť, společná všem běžícím procesům – stav v pracovni/.slusne.json se zámkem flock):
  - dotazy (hledání, API, HTML stránky): nejvýš 1 za 2 s
  - obrázky a dlaždice (podle adresy): nejvýš 10 za 1 s
  - po odpovědi 429 nebo 503 (a po 403 na dotaz) se web na 30 minut zablokuje pro všechny procesy,
    nástroj hned skončí a žádné další pokusy nedělá. Do té doby slusne.py na web nic nepustí.
Omezuje se frekvence, ne souběh – souběžně stahované dlaždice nevadí, vadí série rychlých dotazů.
"""
import fcntl, json, os, re, runpy, shutil, subprocess, sys, tempfile, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "pracovni", ".slusne.json")
SHIM = os.path.join(ROOT, "scripts", "shim")
QUERY_GAP, IMAGE_GAP, BLOCK = 2.0, 0.1, 30 * 60
EXEMPT = {"localhost", "127.0.0.1", "::1", "github.com", "api.github.com", "api.netlify.com",
          "app.netlify.com", "registry.npmjs.org", "pypi.org", "files.pythonhosted.org"}
IMAGE_RX = re.compile(r"\.(jpe?g|png|gif|webp|tiff?)(\?|$)|/image|mrimage|zoomify|tilegroup|/tiles?/|isrv\d*\.cgi|"
                      r"imageproperties|/iiif/|/dao/|action=image|images/", re.I)


def kind_of(url):
    return "image" if IMAGE_RX.search(url or "") else "query"


def _locked(fn):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with open(STATE, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        try:
            st = json.loads(f.read() or "{}")
        except ValueError:
            st = {}
        res = fn(st)
        f.seek(0); f.truncate(); f.write(json.dumps(st)); f.flush()
        return res


def stop(msg):
    sys.stderr.write(f"\n[slusne] {msg}\n")
    sys.stderr.flush()
    os._exit(3)   # i z vlákna: celý nástroj hned končí, žádné další pokusy


def wait_turn(host, kind):
    """Rezervuje další volný čas pro web a počká na něj (zámek se drží jen krátce)."""
    host = (host or "").lower()
    if not host or host in EXEMPT:
        return

    def reserve(st):
        h = st.setdefault(host, {})
        now = time.time()
        if h.get("blocked_until", 0) > now:
            return ("blocked", h["blocked_until"])
        key, gap = ("next_query", QUERY_GAP) if kind == "query" else ("next_image", IMAGE_GAP)
        slot = max(now, h.get(key, 0))
        h[key] = slot + gap
        return ("ok", slot - now)

    state, val = _locked(reserve)
    if state == "blocked":
        stop(f"{host} je dočasně zablokovaný (po odmítnutí serverem) ještě {int((val - time.time()) / 60) + 1} min. "
             f"Nic dalšího se na něj neposílá. Počkej a zkus to pak znovu.")
    if val > 0:
        time.sleep(val)


def check_status(host, kind, status):
    host = (host or "").lower()
    if not host or host in EXEMPT:
        return
    if status in (429, 503) or (status == 403 and kind == "query"):
        def block(st):
            st.setdefault(host, {})["blocked_until"] = time.time() + BLOCK
        _locked(block)
        stop(f"{host} odpověděl {status} – web blokuji na 30 minut pro všechny procesy a končím. "
             f"Žádné další pokusy. Až uplyne pauza, pokračuj pomaleji.")


def patch_http():
    import http.client as hc
    orig_put, orig_get = hc.HTTPConnection.putrequest, hc.HTTPConnection.getresponse

    def putrequest(self, method, url, *a, **kw):
        host = getattr(self, "_tunnel_host", None) or self.host
        m = re.match(r"https?://([^/:]+)", url or "")
        if m and not getattr(self, "_tunnel_host", None):
            host = m.group(1)   # http přes proxy: v url je celá adresa
        self._slusne = (host, kind_of(url))
        wait_turn(host, self._slusne[1])
        return orig_put(self, method, url, *a, **kw)

    def getresponse(self, *a, **kw):
        r = orig_get(self, *a, **kw)
        host, kind = getattr(self, "_slusne", (None, "query"))
        check_status(host, kind, r.status)
        return r

    hc.HTTPConnection.putrequest = putrequest
    hc.HTTPConnection.getresponse = getresponse


def real_curl():
    path = os.pathsep.join(p for p in os.environ.get("PATH", "").split(os.pathsep)
                           if os.path.abspath(p) != os.path.abspath(SHIM))
    c = shutil.which("curl", path=path)
    if not c:
        sys.exit("[slusne] curl nenalezen")
    return c


def run_curl(args):
    urls = [a for a in args if re.match(r"https?://", a)]
    hosts = [(re.match(r"https?://([^/:?]+)", u).group(1), kind_of(u)) for u in urls]
    for h, k in hosts:
        wait_turn(h, k)
    fd, hdr = tempfile.mkstemp(prefix="slusne_hdr_")
    os.close(fd)
    try:
        rc = subprocess.call([real_curl(), "-D", hdr] + args)
        try:
            codes = [int(m) for m in re.findall(r"^HTTP/[\d.]+ (\d{3})", open(hdr, errors="replace").read(), re.M)]
        except OSError:
            codes = []
        codes = [c for c in codes if c != 100]
        if codes and hosts:
            check_status(hosts[-1][0], hosts[-1][1], codes[-1])   # poslední odpověď (po přesměrování)
        return rc
    finally:
        os.unlink(hdr)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "curl":
        sys.exit(run_curl(args))
    if cmd in ("bash", "sh"):
        env = dict(os.environ, PATH=SHIM + os.pathsep + os.environ.get("PATH", ""), SLUSNE=os.path.abspath(__file__))
        sys.exit(subprocess.call([cmd] + args, env=env))
    if not cmd.endswith(".py"):
        sys.exit("[slusne] podporuji: <skript>.py, bash/sh <skript>.sh, curl …")
    patch_http()
    script = os.path.abspath(cmd)
    sys.path.insert(0, os.path.dirname(script))
    sys.argv = [script] + args
    os.environ["PATH"] = SHIM + os.pathsep + os.environ.get("PATH", "")   # i subprocess curl dostane limity
    os.environ["SLUSNE"] = os.path.abspath(__file__)
    runpy.run_path(script, run_name="__main__")


if __name__ == "__main__":
    main()
