#!/usr/bin/env python3
"""PreToolUse hook na Bash: síťová volání na archivy jen přes scripts/slusne.py.

Zamítne (exit 2, důvod jde agentovi):
  - Python se síťovým importem spuštěný mimo slusne.py (soubor, -c i heredoc),
  - curl / wget s adresou mimo localhost mimo slusne.py,
  - shellový skript s curl/wget spuštěný mimo slusne.py.
Je to textová heuristika, ne neprůstřelná ochrana. JavaScript v prohlížeči (Playwright, Claude in Chrome) nevidí.
"""
import json, os, re, sys

NET = re.compile(r"\burllib\.request\b|from\s+urllib\s+import\s+request|\bimport\s+requests\b|\bfrom\s+requests\b|"
                 r"\bhttp\.client\b|\burlopen\s*\(|\bimport\s+socket\b|\bhttpx\b|\baiohttp\b")
LOCAL = re.compile(r"https?://(localhost|127\.0\.0\.1|\[::1\])(:\d+)?(/|$)", re.I)
OK_HOSTS = re.compile(r"https?://([^/\s\"']*\.)?(github\.com|netlify\.com|netlify\.app|npmjs\.org|pypi\.org|pythonhosted\.org)", re.I)
HOW = ("Spusť to přes obal, který hlídá limity archivů:\n"
       "  python3 -I scripts/slusne.py tools/<nastroj>.py …\n"
       "  python3 -I scripts/slusne.py bash tools/<skript>.sh …\n"
       "  python3 -I scripts/slusne.py curl …\n"
       "Vlastní pomocný skript ulož jako soubor a spusť ho stejně: python3 -I scripts/slusne.py cesta/skript.py")


def deny(why):
    sys.stderr.write(f"[slusne-hook] Zamítnuto: {why}\n{HOW}\n")
    sys.exit(2)


def read(path, cwd):
    p = path if os.path.isabs(path) else os.path.join(cwd, path)
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return
    if data.get("tool_name") != "Bash":
        return
    cmd = (data.get("tool_input") or {}).get("command") or ""
    cwd = data.get("cwd") or os.getcwd()
    # části příkazu (; && || | a nové řádky), heredoc obsah zůstává v celém textu
    segments = re.split(r"\n|;|&&|\|\||\|", cmd)

    # 1) curl / wget mimo obal
    for seg in segments:
        if "slusne.py" in seg:
            continue
        if re.search(r"(^|\s|/)(curl|wget)\s", seg + " "):
            urls = re.findall(r"https?://\S+", seg)
            remote = [u for u in urls if not LOCAL.match(u) and not OK_HOSTS.match(u)]
            dynamic = re.search(r"(^|\s)[\"']?\$\{?\w", seg.split("curl", 1)[-1] if "curl" in seg else seg.split("wget", 1)[-1])
            if remote or (dynamic and not urls):
                deny("curl/wget na vzdálený web mimo slusne.py.")

    # 2) Python se síťovým importem mimo obal
    for seg in segments:
        m = re.search(r"\bpython3?(\.\d+)?\b((?:\s+-\S+)*)\s*(\S*)", seg)
        if not m or "slusne.py" in seg:
            continue
        flags, target = m.group(2) or "", m.group(3) or ""
        if target.endswith(".py"):
            if NET.search(read(target, cwd)):
                deny(f"{target} používá síť a běží mimo slusne.py.")
        elif "-c" in flags.split() or target in ("-", "") or "<<" in seg:
            if NET.search(cmd):
                deny("Python se síťovým kódem (-c / heredoc) mimo slusne.py.")

    # 3) shellový skript s curl/wget mimo obal
    for seg in segments:
        if "slusne.py" in seg:
            continue
        for sh in re.findall(r"(?:^|\s)(?:bash|sh)\s+(\S+\.sh)|(?:^|\s)(\.?/\S+\.sh)", seg):
            path = sh[0] or sh[1]
            if re.search(r"\b(curl|wget)\b", read(path, cwd)):
                deny(f"{path} volá curl/wget a běží mimo slusne.py.")


if __name__ == "__main__":
    main()
