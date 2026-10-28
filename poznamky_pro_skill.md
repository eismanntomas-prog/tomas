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
