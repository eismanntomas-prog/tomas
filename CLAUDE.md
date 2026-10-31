# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Slušné stahování z archivů (ochrana před banem)
- Každý nástroj, který stahuje z archivů, spouštěj přes obal: `python3 -I scripts/slusne.py tools/<nastroj>.py …`,
  shellové skripty `python3 -I scripts/slusne.py bash tools/<skript>.sh …`, jednotlivý curl `python3 -I scripts/slusne.py curl …`.
- Obal hlídá limity pro každý web zvlášť a společně pro všechny procesy: dotazy 1 za 2 s, obrázky/dlaždice 10 za s.
  Po odpovědi 429/503 (a 403 na dotaz) web na 30 minut zablokuje a nástroj skončí – NEZKOUŠEJ to znovu ani jinou cestou, počkej.
- Hook v `.claude/settings.json` zamítne síťový Python, curl/wget a shellové skripty s curl spuštěné mimo obal.
- Prohlížeč (Playwright, Claude in Chrome) hook nevidí: tam ručně nejvýš 1 dotaz za 2 s, žádné `Promise.all` ani paralelní dotazy.
