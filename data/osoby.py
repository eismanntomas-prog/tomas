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
    3: dict(n="Hana Spálenková", y="* 1948", st="fam", f=["* 1948 Praha (?)", "provdaná Eismannová"], r=[], note="Žijící – údaje jen základní."),
    6: dict(n="Václav Spálenka", y="* 1916", st="doc", f=["* 11. 11. 1916 Ouběnice č. 25 (okr. Benešov)", "obchodní příručí v koloniálním obchodě, Praha XII, Koubkova 16 (1942)", "× 17. 10. 1942 Votice Antonie Vrzalová", "později bydliště Počernice (Praha)"], r=["vot_snatek_vaclav_spalenka_antonie_vrzalova_1942"], deti=["Jiří (bratr maminky Hany)"]),
    7: dict(n="Antonie Vrzalová", y="* 1921", st="doc", f=["* 23. 4. 1921 Městečko č. 3 (obec Olbramovice)", "× 17. 10. 1942 Votice Václav Spálenka", "později bydliště Počernice (Praha)"], r=["vot_snatek_vaclav_spalenka_antonie_vrzalova_1942"], deti=["Jiří (bratr maminky Hany)"]),
    12: dict(n="Jan Spálenka", y="1878–1931", st="doc", f=["* 27. 2. 1878 Střížovec č. 2 (fara Ouběnice)", "domkář, chalupník a rolník v Ouběnicích č. 25", "× 17. 11. 1908 Ouběnice Kateřina Hovorková", "† 23. 4. 1931 Benešov (nemocnice), pohřben v Ouběnicích"], r=["oub_krest_jan_spalenka_1878","oub_umrti_jan_spalenka_1931","oub_snatek_jan_spalenka_katerina_hovorkova_1908","vot_snatek_vaclav_spalenka_antonie_vrzalova_1942"], deti=["Marie (1911–1912)", "Jan (1913–1940)"]),
    13: dict(n="Kateřina Hovorková", y="1881–1950", st="doc", f=["* 6. 3. 1881 Kobylí č. 8", "× 17. 11. 1908 Ouběnice Jan Spálenka", "† 13. 11. 1950 Praha"], deti=["Marie (* 1911, † 1912)", "Jan (* 1913, † 1940)", "Liduše (dle rodiny; žila v Praze)"], r=["oub_krest_katerina_hovorkova_1881","oub_snatek_jan_spalenka_katerina_hovorkova_1908","vot_snatek_vaclav_spalenka_antonie_vrzalova_1942"]),
    24: dict(n="Josef Spálenka", y="1842–1908", st="doc", f=["* 6. 3. 1842 (místo: Nadějkov? č. 3)", "domkář ve Střížovci č. 2", "× 30. 5. 1871 Bystřice (Tožice) Marie Medalová", "† 7. 1. 1908 Střížovec č. 2 (65 let), pohřben v Ouběnicích"], deti=["Anna (* 1880)", "František (* 1882)", "Václav (* 1885)", "Josefa (* 1889)", "Bohumil (* 1891)"], r=["oub_umrti_josef_spalenka_1908","bys_snatek_josef_spalenka_marie_medalova_1871","oub_krest_jan_spalenka_1878","oub_snatek_jan_spalenka_katerina_hovorkova_1908"], note="Další děti ve Střížovci č. 2: Anna 1880, František 1882, Václav 1885, Josefa 1889, Bohumil 1891."),
    25: dict(n="Marie Medalová", y="* asi 1852", st="doc", f=["z Tožice č. 9", "× 30. 5. 1871 Josef Spálenka"], deti=["Anna (* 1880)", "František (* 1882)", "Václav (* 1885)", "Josefa (* 1889)", "Bohumil (* 1891)"], r=["bys_snatek_josef_spalenka_marie_medalova_1871","oub_krest_jan_spalenka_1878","oub_snatek_jan_spalenka_katerina_hovorkova_1908"]),
    48: dict(n="Josef Spálenka", y="† před 1878", st="doc", f=["z Nadějkova (?) č. 3", "domkář ve Střížovci č. 2"], r=["oub_umrti_josef_spalenka_1908","bys_snatek_josef_spalenka_marie_medalova_1871","oub_krest_jan_spalenka_1878"]),
    49: dict(n="Josefa Kocourová (?)", y="* ?", st="doc", f=["z Nadějkova (?) č. 5"], r=["oub_umrti_josef_spalenka_1908","oub_krest_jan_spalenka_1878"], note="Příjmení i obec čteny nejistě."),
    50: dict(n="Jan Medal", y="* ?", st="doc", f=["kovář v Tožici č. 9"], r=["bys_snatek_josef_spalenka_marie_medalova_1871","oub_krest_jan_spalenka_1878"]),
    102: dict(n="Matěj Tiš", y="* ?", st="doc", f=["kovář v Obrouhlici č. 7"], r=["bys_snatek_josef_spalenka_marie_medalova_1871"]),
    103: dict(n="Anna Kolářová (?)", y="* ?", st="doc", f=["z Obrouhlice č. 7"], r=["bys_snatek_josef_spalenka_marie_medalova_1871"], note="Příjmení čteno nejistě."),
    51: dict(n="Anna Tišová", y="* ?", st="doc", f=["z Obrouhlice č. 7"], r=["oub_krest_jan_spalenka_1878"]),
    26: dict(n="Jan Hovorka", y="* ?", st="doc", f=["rolník v Kobylí č. 8 (svobodnická ves)"], deti=["Jan (svědek na svatbě sestry 1908)"], r=["oub_krest_katerina_hovorkova_1881","oub_snatek_jan_spalenka_katerina_hovorkova_1908"]),
    27: dict(n="Josefa Dvořáková", y="* ?", st="doc", f=["z Kobylí č. 9"], deti=["Jan (svědek na svatbě sestry 1908)"], r=["oub_krest_katerina_hovorkova_1881","oub_snatek_jan_spalenka_katerina_hovorkova_1908"]),
    14: dict(n="Tomáš Vrzal", y="1874–1936", st="doc", f=["* 24. 12. 1874 Městečko č. 3 (Olbramovice)", "rolník v Městečku č. 3", "× 26. 1. 1909 Vrchotovy Janovice Antonie Dalihodová", "† 12. 8. 1936 na cestě u Tábora, pohřben v Olbramovicích"], r=["vot_krest_tomas_vrzal_1874","vj_snatek_tomas_vrzal_antonie_dalihodova_1909","vot_umrti_tomas_vrzal_1936","vot_snatek_vaclav_spalenka_antonie_vrzalova_1942"], note="Datum narození: křestní matrika 24. 12. 1874, oddací (1909) i úmrtní (1936) zápis 24. 4. 1874.", deti=["Božena (* 1910, Městečko – číslo domu v rejstříku nečitelné, pravděpodobně)", "Marie (* 1912, Městečko 3 nebo 8 – nejisté čtení)", "Anna (* 1914, Městečko 3)", "Vojtěch (* 1917, Městečko 3)", "Anežka (* 1925, Městečko 3)"]),
    52: dict(n="Antonín Hovorka", y="* ?", st="doc", f=["rolník, 1881 výměnkář v Kobylí č. 8"], r=["oub_krest_katerina_hovorkova_1881"]),
    53: dict(n="Anna Dvořáková", y="* ?", st="doc", f=["z Kobylí č. 10"], r=["oub_krest_katerina_hovorkova_1881"]),
    54: dict(n="Josef Dvořák", y="† před 1881", st="doc", f=["rolník v Kobylí č. 9"], r=["oub_krest_katerina_hovorkova_1881"]),
    55: dict(n="Marie Vosátková (?)", y="* ?", st="doc", f=["z Hlohova č. 12"], r=["oub_krest_katerina_hovorkova_1881"], note="Příjmení čteno nejistě."),
    28: dict(n="Vojtěch Vrzal", y="1844–1909", st="doc", f=["* 12. 7. 1844 Městečko č. 3 (Olbramovice)", "gruntovník (rolník) v Městečku č. 3", "× 3. 2. 1874 Votice Františka Lupáčová", "1909 na výminku", "† 3. 10. 1909 Městečko č. 3, pohřben v Olbramovicích"], deti=["Marie († 1892, Městečko 3 – snad dcera, neověřeno)"], r=["vot_krest_vojtech_vrzal_1844","vot_umrti_vojtech_vrzal_1909","vot_snatek_vojtech_vrzal_frantiska_lupacova_1874","vot_krest_tomas_vrzal_1874"]),
    29: dict(n="Františka Lupáčová", y="1850–1926", st="doc", f=["ze Semtína č. 5", "× 3. 2. 1874 Votice Vojtěch Vrzal", "† 27. 1. 1926 Městečko č. 3 (výminkářka), pohřbena v Olbramovicích"], r=["vot_snatek_vojtech_vrzal_frantiska_lupacova_1874","vot_krest_tomas_vrzal_1874","vot_umrti_frantiska_vrzalova_1926"]),
    60: dict(n="František Dalihod", y="† před 1884", st="doc", f=["rolník v Radotíně č. 10"], r=["vj_krest_antonie_dalihodova_1884"]),
    61: dict(n="Kateřina Červenková", y="* ?", st="doc", f=["z Průhonic"], r=["vj_krest_antonie_dalihodova_1884"]),
    62: dict(n="Jan Hluchovský", y="* ?", st="doc", f=["sedlák ve Slavkově č. 1"], r=["vj_krest_antonie_dalihodova_1884"]),
    63: dict(n="Kateřina Votrubová", y="* ?", st="doc", f=["ze Slavkova č. 1"], r=["vj_krest_antonie_dalihodova_1884"]),
    56: dict(n="Václav Vrzal", y="1812 – před 1873", st="doc", f=["* 2. 6. 1812 Městečko č. 3 (Olbramovice)", "sedlák (gruntovník) v Městečku č. 3", "† před 10. 4. 1873 (v úmrtním zápisu manželky uveden jako zesnulý)", "× 14. 11. 1837 Votice Rosálie Macháčková"], r=["vot_umrti_rosalie_vrzalova_1873","vot_krest_vaclav_vrzal_1812","vot_snatek_vaclav_vrzal_rosalie_machackova_1837","vot_krest_vojtech_vrzal_1844","vot_snatek_vojtech_vrzal_frantiska_lupacova_1874","vot_krest_tomas_vrzal_1874"], deti=["Václav (* 1846)", "Marie Dorota (* 1849)", "Josefa (* 1850)", "Marie (* 1852)"]),
    57: dict(n="Rosalie Macháčková", y="1815–1873", st="doc", f=["* 8. 4. 1815 Velký Semtín č. 11 (pokřtěna 9. 4.)", "× 14. 11. 1837 Votice Václav Vrzal", "† 10. 4. 1873 Městečko č. 3, pohřbena v Olbramovicích"], deti=["Václav (* 1846)","Marie Dorota (* 1849)","Josefa (* 1850)","Marie (* 1852)"], r=["vot_krest_rosalie_machackova_1815","vot_umrti_rosalie_vrzalova_1873","vot_snatek_vaclav_vrzal_rosalie_machackova_1837","vot_krest_vojtech_vrzal_1844","vot_snatek_vojtech_vrzal_frantiska_lupacova_1874","vot_krest_tomas_vrzal_1874"]),
    112: dict(n="Václav Vrzal", y="* asi 1782", st="doc", f=["* asi 1782 (dle věku při sňatku)", "sedlák v Městečku č. 3, poddaný panství Janovice/Votice", "× 7. 5. 1811 Votice Anna Laštovková (?)", "1844 na výminku", "† po 1844 (datum nedohledáno)"], deti=["Václav (* 1812)"], r=["vot_snatek_vaclav_vrzal_anna_lastovkova_1811","vot_krest_vaclav_vrzal_1812","vot_snatek_vaclav_vrzal_rosalie_machackova_1837","vot_krest_vojtech_vrzal_1844"]),
    113: dict(n="Anna Laštovková (?)", y="* asi 1791", st="doc", f=["z Kaliště", "dcera Matěje Laštovky (?), sedláka"], r=["vot_snatek_vaclav_vrzal_anna_lastovkova_1811","vot_krest_vaclav_vrzal_1812","vot_snatek_vaclav_vrzal_rosalie_machackova_1837","vot_krest_vojtech_vrzal_1844"], note="Příjmení čteno nejistě (Rybková? Laštovková?); otec Matěj, sedlák v Kališti."),
    114: dict(n="Vojtěch Macháček", y="asi 1778–po 1837", st="doc", f=["* asi 1778 (dle věku při sňatku)","sedlák ve Velkém Semtíně č. 11","× 2. 10. 1798 Votice Kateřina Lupáčová","1837 živ (dal souhlas ke svatbě dcery)"], r=["vot_snatek_vojtech_machacek_katerina_lupacova_1798","vot_krest_rosalie_machackova_1815","vot_snatek_vaclav_vrzal_rosalie_machackova_1837","vot_krest_vojtech_vrzal_1844"]),
    115: dict(n="Kateřina Lupáčová", y="asi 1781–?", st="doc", f=["* asi 1781 (dle věku při sňatku)","z Mokřan, dcera Tomáše Lupáče","× 2. 10. 1798 Votice Vojtěch Macháček"], r=["vot_snatek_vojtech_machacek_katerina_lupacova_1798","vot_krest_rosalie_machackova_1815","vot_snatek_vaclav_vrzal_rosalie_machackova_1837","vot_krest_vojtech_vrzal_1844"]),
    58: dict(n="Josef Lupáč", y="* ?", st="doc", f=["gruntovník ze Semtína č. 5"], r=["vot_snatek_vojtech_vrzal_frantiska_lupacova_1874","vot_krest_tomas_vrzal_1874"]),
    59: dict(n="Kateřina Zoulová", y="* ?", st="doc", f=["z Křešic"], r=["vot_snatek_vojtech_vrzal_frantiska_lupacova_1874","vot_krest_tomas_vrzal_1874"]),
    15: dict(n="Antonie Dalihodová", y="* 1884", st="doc", f=["* 28. 3. 1884 Radotín č. 10 (Olbramovice)", "× 26. 1. 1909 Vrchotovy Janovice Tomáš Vrzal", "selka na statku Městečko č. 3", "1936 ovdověla", "v úmrtním rejstříku Votic do 1949 není"], r=["vj_krest_antonie_dalihodova_1884","vj_snatek_tomas_vrzal_antonie_dalihodova_1909","vot_snatek_vaclav_spalenka_antonie_vrzalova_1942"], deti=["Božena (* 1910, Městečko – číslo domu v rejstříku nečitelné, pravděpodobně)", "Marie (* 1912, Městečko 3 nebo 8 – nejisté čtení)", "Anna (* 1914, Městečko 3)", "Vojtěch (* 1917, Městečko 3)", "Anežka (* 1925, Městečko 3)"]),
    30: dict(n="František Dalihod", y="* ?", st="doc", f=["rolník v Radotíně č. 10 (1884), později ve Slavkově č. 1"], r=["vj_krest_antonie_dalihodova_1884","vj_snatek_tomas_vrzal_antonie_dalihodova_1909"]),
    31: dict(n="Marie Hluchovská", y="* ?", st="doc", f=["ze Slavkova č. 1"], r=["vj_krest_antonie_dalihodova_1884","vj_snatek_tomas_vrzal_antonie_dalihodova_1909"]),
    4: dict(n="František Eismann", y="asi 1905/06 – 1988", st="fam", f=["bankovní úředník", "bydliště Praha-Vinohrady", "† 1988 (ve věku asi 82 let)", "pohřben Vinohradský hřbitov, odd. 48, hrob 219"], r=[],
            note="Od rodiny: zemřel 1988, nejspíš ve věku 82 let → nar. asi 1905–1906. Rodina říká, že jeho větev pochází z Hudlic u Berouna. Kandidát z policejní přihlášky 1907 (František Eismann * 1905, syn Boženy roz. Hamelové, vdovy po hasiči, domovská obec Těnovice u Plzně) teď věkem sedí; rozpor je jen v domovské obci (Těnovice × Hudlice) – ověřit."),
    5: dict(n="Vlasta Nová", y="* 1912", st="doc", f=["* 26. 1. 1912 České Budějovice, Haasova ul. č. 42", "1922 vystoupila z církve (bez vyznání)", "bydliště Praha-Vinohrady"], r=["cb_krest_vlasta_nova_1912"],
            note="Rodina: Vlasta Nová, * asi 1912 v Č. Budějovicích, měla bratra Slávka. Jediná Vlasta Nová v rejstříku sv. Mikuláše 1910–1914; bratr Stanislav * 1913 nalezen u stejných rodičů. Sňatek s Františkem Eismannem zatím nedoložen."),
    10: dict(n="Stanislav Nový", y="* 1886", st="doc", f=["* 28. 4. 1886 Heinrichsbrunn č. 15, okr. Perg (Horní Rakousy)", "pozlacovač v Českých Budějovicích", "× 25. 2. 1911 České Budějovice Marie Cikánková"], r=["cb_snatek_stanislav_novy_marie_cikankova_1911","cb_krest_vlasta_nova_1912"], note="Datum a místo narození z oddacího zápisu (křestní list fary Mauthausen). Vlastní křest na Matricule zatím neověřen."),
    11: dict(n="Marie Cikánková", y="* 1887", st="doc", f=["* 25. 8. 1887 České Budějovice, Nová ulice č. 29", "× 25. 2. 1911 České Budějovice Stanislav Nový", "1921 vystoupila z církve"], r=["cb_krest_marie_cikankova_1887","cb_snatek_stanislav_novy_marie_cikankova_1911","cb_krest_vlasta_nova_1912"]),
    20: dict(n="Jan Nový", y="* ?", st="doc", f=["strojní zámečník v Českých Budějovicích"], r=["cb_snatek_stanislav_novy_marie_cikankova_1911"]),
    21: dict(n="Rozálie Praschek (?)", y="* ?", st="doc", f=["z Urtinovic (?), okres Budějovice"], r=["cb_snatek_stanislav_novy_marie_cikankova_1911"], note="Příjmení i obec čteny nejistě (Raschek/Praschek; Urtinovice?)."),
    22: dict(n="Jan Cikánek", y="* 1856", st="doc", f=["* 24. 12. 1856 Veselí nad Lužnicí č. 56", "× 24. 5. 1886 České Budějovice Marie Semmelbauerová", "kovář (?) 1886; později topič v tabákové továrně v Českých Budějovicích"], r=["cb_snatek_jan_cikanek_marie_semmelbauerova_1886","ves_krest_jan_cikanek_1856","cb_krest_marie_cikankova_1887","cb_snatek_stanislav_novy_marie_cikankova_1911"]),
    23: dict(n="Marie Semmelbauerová", y="* 1858", st="doc", f=["* 25. 6. 1858 Čtyři Dvory č. 1", "× 24. 5. 1886 České Budějovice Jan Cikánek"], r=["cb_snatek_jan_cikanek_marie_semmelbauerova_1886","cd_krest_marie_semmelbauerova_1858","cb_krest_marie_cikankova_1887"], note="Nemanželská dcera Veroniky Semmelbauerové."),
    44: dict(n="Matěj Cikánek", y="* 1823", st="doc", f=["* 23. 2. 1823 Veselí nad Lužnicí č. 65", "podruh ve Veselí nad Lužnicí č. 56"], r=["ves_krest_matej_cikanek_1823","ves_krest_jan_cikanek_1856","cb_krest_marie_cikankova_1887"], note="Nemanželský syn Marie Cikánkové. Sňatek s Dorotou Dvořákovou kolem 1855 (výpis z matriky 10. 11. 1855) – ve Veselí 9/1855–4/1856 nenalezen."),
    45: dict(n="Dorota Dvořáková", y="* ?", st="doc", f=["z Vlkova"], r=["ves_krest_jan_cikanek_1856","cb_krest_marie_cikankova_1887"], note="Dcera Jana Dvořáka a Anny (roz. Kouba?) – čteno nejistě."),
    88: dict(n="otec neuveden", st="unk", f=[], note="Matěj Cikánek nese příjmení matky."),
    89: dict(n="Marie Cikánková", y="* ?", st="doc", f=["podruhyně ve Veselí nad Lužnicí č. 56"], r=["ves_krest_matej_cikanek_1823","ves_krest_jan_cikanek_1856"], note="Dcera Matěje Cikánka, zedníka (?) z Horusic (?), a Kateřiny."),
    178: dict(n="Matěj Cikánek", y="† před 1823", st="doc", f=["zedník (?) z Horusic (?)"], r=["ves_krest_matej_cikanek_1823"], note="Řemeslo a obec čteny nejistě."),
    179: dict(n="Kateřina ?", y="* ?", st="doc", f=[], r=["ves_krest_matej_cikanek_1823"]),
    90: dict(n="Jan Dvořák", y="* ?", st="doc", f=["z Vlkova (?)"], r=["ves_krest_jan_cikanek_1856"]),
    91: dict(n="Anna Koubová (?)", y="* ?", st="doc", f=[], r=["ves_krest_jan_cikanek_1856"], note="Rodné příjmení čteno nejistě."),
    46: dict(n="otec neuveden", st="unk", f=[], note="Marie Semmelbauerová byla podle zápisu dcerou Veroniky; otec neuveden."),
    47: dict(n="Veronika Semmelbauerová", y="* ?", st="doc", f=["Čtyři Dvory"], r=["cd_krest_marie_semmelbauerova_1858","cb_krest_marie_cikankova_1887"]),
    94: dict(n="Ondřej Semmelbauer", y="* ?", st="doc", f=["nádeník ve Čtyřech Dvorech"], r=["cd_krest_marie_semmelbauerova_1858","cb_krest_marie_cikankova_1887"]),
    95: dict(n="Marie Čížková", y="* ?", st="doc", f=[], r=["cd_krest_marie_semmelbauerova_1858","cb_krest_marie_cikankova_1887"]),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
    12: ("Spálenkové", "Rolníci z Ouběnic u Bystřice (Benešovsko). Václav Spálenka (* 1916) odešel do Prahy jako obchodní příručí."),
    14: ("Vrzalové", "Rolníci z Městečka u Olbramovic (Voticko)."),
    8: ("Eismannové", "Rod dědečka Františka, bankovního úředníka na Vinohradech. Podle rodiny pochází z Hudlic u Berouna – zatím neověřeno."),
    10: ("Noví", "Stanislav Nový, pozlacovač, přišel do Českých Budějovic z Horního Rakouska (Heinrichsbrunn u Mauthausenu)."),
    11: ("Cikánkové", "Podruzi z Veselí nad Lužnicí; Jan Cikánek odešel do Budějovic za prací v tabákové továrně a vzal si Marii Semmelbauerovou ze Čtyř Dvorů."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=12, n="Sourozenci Jana Spálenky", t="Děti Josefa Spálenky a Marie Medalové ze Střížovce č. 2 podle rejstříku narozených Ouběnice: Anna (* 1880), František (* 1882), Václav (* 1885), Josefa (* 1889), Bohumil (* 1891).", r=[]),
    dict(k=6, n="Marie Spálenková (1911–1912)", t="Starší sestra Václava, * 4. 8. 1911 v Ouběnicích č. 25, zemřela v 8 měsících na zápal plic.", r=["oub_umrti_marie_spalenkova_1912"]),
    dict(k=6, n="Jan Spálenka (1913–1940)", t="Starší bratr Václava, * 22. 8. 1913 v Ouběnicích č. 25, úředník benešovské nemocnice; zemřel svobodný ve 26 letech na zánět ledvin.", r=["oub_umrti_jan_spalenka_1940"]),
    dict(k=7, n="Sourozenci Antonie Vrzalové", t="Podle rejstříku narozených farnosti Votice: Božena (* 1910), Marie (* 1912), Anna (* 1914), Vojtěch (* 1917), Anežka (* 1925); u Boženy a Marie je číslo domu nejisté.", r=[]),
    dict(k=28, n="Sourozenci Vojtěcha Vrzala", t="Podle rejstříku narozených Votic 1843–1855 (Městečko č. 3): Václav (* 1846), Marie Dorota (* 1849), Josefa (* 1850), Marie (* 1852).", r=[]),
    dict(k=112, n="Hypotéza: původ Václava Vrzala (* asi 1782)", t="Kniha Votice 06 (Městečko a okolí 1771–1786) prošla celá; Václav Vrzal narozený 1777–1786 v ní není. Kandidáti: (1) Václav * 20. 11. 1776, syn Jakuba Vrzala, sedláka, a Veroniky roz. Batounkové? (dům č. 2) – v roce 1811 by mu bylo 34, ne 29; (2) syn Václava Vrzala a Doroty roz. Marvanové (děti v Městečku 1777–1783). Neověřeno.", r=[]),
    dict(k=112, n="Sourozenci Václava Vrzala (* 1812)", t="Ze statku Městečko č. 3 (otec Václav, matka Anna): Pozor: Veronika * 1805, František Xaver * 1807, František * 1808 jsou starší než sňatek 1811 – jsou to děti jiného Vrzala z č. 3 (snad svědka Františka Vrzala) nebo z prvního manželství; ověřit (Votice N 1788–1813).", r=[]),
    dict(k=14, n="Antonín Vrzal (* asi 1870–1885)", t="Svědek na svatbě Tomáše Vrzala 1909, strojník ve Vídni III – nejspíš Tomášův bratr.", r=["vj_snatek_tomas_vrzal_antonie_dalihodova_1909"]),
    dict(k=1, n="Petr Eismann", t="Bratr Tomáše. Žijící – údaje jen základní.", r=[]),
    dict(k=3, n="Jiří Spálenka", t="Bratr maminky Hany, syn Václava a Antonie Spálenkových. Žijící / údaje jen základní.", r=[]),
    dict(k=5, n="Stanislav (Slávek) Nový (* 1913)", t="Mladší bratr babičky Vlasty, * 1. 9. 1913 v Českých Budějovicích, Haasova ul. 42. Podle rodiny „Slávek“.", r=["cb_krest_stanislav_novy_1913"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Souvisí dědeček František Eismann s učitelským rodem Eismannů ze Zdic a Hudlic?", "Hypotéza: tři generace učitelů Václavů Eismannů (Zdice, Zvíkovec); Václav * 1871 Zdice, jeho děd z matčiny strany Jan Males byl učitelem v Hudlicích (rodinná tradice: předek-učitel v Hudlicích). Spojení s Františkem * asi 1905 (přihláška 1907: matka Božena roz. Hamelová, vdova po hasiči, domovská obec Těnovice) zatím nedoloženo."),
    ("Kde se brali Matěj Cikánek a Dorota Dvořáková (kolem 1855)?", "Otevřené: ve Veselí n. L. (1855–1857) ani ve Vlkově nenalezeno; Dorotino rodiště je v zápisu čteno nejistě."),
    ("Odkud přišli Semmelbauerovi do Čtyř Dvorů?", "Otevřené: Veronika se ve Čtyřech Dvorech (1785–1852) nenarodila; domovská obec Ondřeje Semmelbauera zatím nepřečtena."),
    ("Kde byl pokřtěn Stanislav Nový (* 1886)?", "Otevřené: fara Mauthausen (Horní Rakousy), matriky na portálu Matricula – zatím neověřeno."),
    ("Je dědeček František Eismann totožný s Františkem * 1905, synem Boženy roz. Hamelové?", "Hypotéza (dědeček zemřel 1988 ve věku asi 82 let, tj. nar. asi 1905–1906 – věkem sedí na přihlášku; rodina zmiňuje Hudlice u Berouna, přihláška Těnovice u Plzně): policejní přihláška 1907 uvádí Boženu Eismannovou roz. Hamel (* 1878), vdovu po hasiči, s dětmi Marií (* 1903) a Františkem (* 1905); domovská obec Těnovice, okres Plzeň. Potvrdit sňatkem Františka a Vlasty."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
