# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


- 2026-10-28: policie_prihlasky.py – „karta“ hlásí „nenalezena“, protože portál vrací obrázky s příponou `.JPG` (velkými).
  Oprava: v regexu v karta() přidat `re.I`.
- 2026-10-28: trebon.py misto "Ceske Budejovice" vrací synagogu; katolické knihy sv. Mikuláše jsou dohledatelné přes předměstí
  (misto "Nemanice" → svazky) nebo přímo id knih: N 2711–2750 + 9492–9504, O 2771–2787 + 9505–9510, Z 2801–2821 + 9511–9513.
  Oddací knihy nemají dobrovolnický rejstřík, ale mají vlastní rejstřík ženichů na konci knihy.
- 2026-10-29: Netlify web eclectic-pudding-ca9d03 je napojený na GitHub repozitář (auto-build při každém pushi z kořene repozitáře → „Page not found“,
  protože kořen nemá index.html). Řešení: nasazení z web/dist přes `netlify deploy --prod --dir=dist` (v cloudu s NODE_USE_ENV_PROXY=1) a zamčení nasazení
  (`netlify api lockDeploy`), aby ho push nepřepsal. Odemknout: Netlify → Deploys → „Start auto publishing“.
  Skill by měl před nasazením zkontrolovat, jestli není web napojený na git (listSiteDeploys → branch/commit_ref).
- 2026-10-31: přidán scripts/slusne.py (limity 1 dotaz/2 s, 10 obrázků/s na web, blokace 30 min po 429/503/403, stav ve flock souboru),
  shim scripts/shim/curl a PreToolUse hook .claude/hooks/slusne_hook.py. Návrh: zařadit do šablony skillu.
