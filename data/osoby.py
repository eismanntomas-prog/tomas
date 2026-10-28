# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
    1: dict(n="Tomáš Eismann", y="* 1985", st="fam", sex="M", f=["* 1985 Praha"], r=[], note="Žijící – údaje jen základní."),
    2: dict(n="Zdeněk Eismann", y="* 1945", st="fam", f=["* 1945 Praha"], r=[], note="Údaje jen základní (narozen 1945, matrika zatím není veřejná)."),
    4: dict(n="František Eismann", y="* ?", st="fam", f=["bankovní úředník", "bydliště Praha-Vinohrady"], r=[],
            note="Od rodiny. Hypotéza: totožný s Františkem Eismannem * 1905 z policejní přihlášky 1907 (karton 3, obraz 781) – ověřit."),
    5: dict(n="Vlasta Nová", y="* 1912", st="doc", f=["* 26. 1. 1912 České Budějovice, Haasova ul. č. 42", "1922 vystoupila z církve (bez vyznání)", "bydliště Praha-Vinohrady"], r=["cb_krest_vlasta_nova_1912"],
            note="Rodina: Vlasta Nová, * asi 1912 v Č. Budějovicích. Jediná Vlasta Nová v rejstříku sv. Mikuláše 1910–1914. Spojení se sňatkem s Františkem Eismannem zatím nedoloženo."),
    10: dict(n="Stanislav Nový", y="* ?", st="doc", f=["pozlacovač v Českých Budějovicích", "* Heinrichsbrunn(?) č. 15"], r=["cb_krest_vlasta_nova_1912"], note="Místo narození čteno nejistě."),
    11: dict(n="Marie Šikánková (?)", y="* ?", st="doc", f=["* České Budějovice"], r=["cb_krest_vlasta_nova_1912"], note="Příjmení otce čteno nejistě (Šikánek?)."),
    20: dict(n="Jan Nový", y="* ?", st="doc", f=["strojní zámečník v Českých Budějovicích"], r=["cb_krest_vlasta_nova_1912"]),
    21: dict(n="Rozalie Raschek (?)", y="* ?", st="doc", f=["z Urtinovic(?)"], r=["cb_krest_vlasta_nova_1912"], note="Příjmení i místo čteno nejistě."),
    22: dict(n="Jan Šikánek (?)", y="* ?", st="doc", f=["topič v tabákové továrně v Č. Budějovicích"], r=["cb_krest_vlasta_nova_1912"]),
    23: dict(n="Marie Semmelbauerová", y="* ?", st="doc", f=["ze Čtyř Dvorů č. 1"], r=["cb_krest_vlasta_nova_1912"]),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Je dědeček František Eismann totožný s Františkem * 1905, synem Boženy roz. Hamelové?", "Hypotéza: policejní přihláška 1907 uvádí Boženu Eismannovou roz. Hamel (* 1878), vdovu po hasiči, s dětmi Marií (* 1903) a Františkem (* 1905); domovská obec Těnovice, okres Plzeň. Potvrdit sňatkem Františka a Vlasty."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
