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
    10: dict(n="Stanislav Nový", y="* 1886", st="doc", f=["* 28. 4. 1886 Heinrichsbrunn č. 15, okr. Perg (Horní Rakousy)", "pozlacovač v Českých Budějovicích", "× 25. 2. 1911 České Budějovice Marie Cikánková"], r=["cb_snatek_stanislav_novy_marie_cikankova_1911","cb_krest_vlasta_nova_1912"], note="Datum a místo narození z oddacího zápisu (křestní list fary Mauthausen). Vlastní křest na Matricule zatím neověřen."),
    11: dict(n="Marie Cikánková", y="* 1887", st="doc", f=["* 25. 8. 1887 České Budějovice, Nová ulice č. 29", "× 25. 2. 1911 České Budějovice Stanislav Nový", "1921 vystoupila z církve"], r=["cb_krest_marie_cikankova_1887","cb_snatek_stanislav_novy_marie_cikankova_1911","cb_krest_vlasta_nova_1912"]),
    20: dict(n="Jan Nový", y="* ?", st="doc", f=["strojní zámečník v Českých Budějovicích"], r=["cb_snatek_stanislav_novy_marie_cikankova_1911"]),
    21: dict(n="Rozálie Praschek (?)", y="* ?", st="doc", f=["z Urtinovic (?), okres Budějovice"], r=["cb_snatek_stanislav_novy_marie_cikankova_1911"], note="Příjmení i obec čteny nejistě (Raschek/Praschek; Urtinovice?)."),
    22: dict(n="Jan Cikánek", y="* ?", st="doc", f=["* Veselí č. 56", "topič v tabákové továrně v Českých Budějovicích"], r=["cb_krest_marie_cikankova_1887","cb_snatek_stanislav_novy_marie_cikankova_1911"], note="Veselí – nejspíš Veselí nad Lužnicí (matka z nedalekého Vlkova)."),
    23: dict(n="Marie Semmelbauerová", y="* ?", st="doc", f=["* Čtyři Dvory č. 1"], r=["cb_krest_marie_cikankova_1887"], note="Podle křtu dcery byla dcerou Veroniky Semmelbauerové; otec neuveden (asi nemanželská)."),
    44: dict(n="Matěj Cikánek", y="* ?", st="doc", f=["podruh ve Veselí č. 56"], r=["cb_krest_marie_cikankova_1887"]),
    45: dict(n="Dorota Dvořáková", y="* ?", st="doc", f=["z Vlkova"], r=["cb_krest_marie_cikankova_1887"]),
    46: dict(n="otec neuveden", st="unk", f=[], note="Marie Semmelbauerová byla podle zápisu dcerou Veroniky; otec neuveden."),
    47: dict(n="Veronika Semmelbauerová", y="* ?", st="doc", f=["Čtyři Dvory"], r=["cb_krest_marie_cikankova_1887"]),
    94: dict(n="Ondřej Semmelbauer", y="* ?", st="doc", f=["nádeník ve Čtyřech Dvořích"], r=["cb_krest_marie_cikankova_1887"]),
    95: dict(n="Marie Čížková", y="* ?", st="doc", f=[], r=["cb_krest_marie_cikankova_1887"]),
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
