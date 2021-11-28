"""
Izberi si primeren zapis za beleženje telefonskega imenika, kjer
hranimo podatek o imenu osebe in njegovi telefonski številki.

Pri tem upoštevaj:
- želimo iskati telefonske številke glede na ime osebe
- želimo dodajati nove osebe in brisati obstoječe
- želimo spreminjati telefonske številke
"""

"""
Napiši funkcijo poisci, ki kot argument sprejme imenik in
ime osebe. V primeru, da oseba obstaja, funkcija vrne njeno
telefonsko številko, če oseba v imeniku ne obstaja naj funkcija
vrne False.
"""

"""
Napiši funkcijo dodaj, ki kot argument sprejme imenik, ime osebe
in njeno telefonsko številko. Funkcija vnos doda v imenik le v primeru,
da oseba v imeniku še ne obstaja. Sicer naj izpiše, da oseba že obstaja.
"""

"""
Zgled: Napiši funkcijo popravi, ki kot argument sprejme imenik, ime osebe
in njeno telefonsko številko. Funkcija spremeni telefonsko številko le
v primeru, da oseba v imeniku že obstaja.
"""

"""
Zgled: Napiši funkcijo izbrisi, ki kot argument sprejme imenik in ime osebe.
Če oseba v imeniku obstaja, naj jo funkcija izbriše, sicer naj javi, da te
osebe ni v imeniku.
"""

"""
Zgled: Napiši funkcijo izpisi_slovar, ki kot argument sprejme imenik in tega
izpise po vrsticah v obliki ime osebe: telefonska stevilka.
"""

"""
Napiši funkcijo izpisi_urejeno, ki kot argument sprejme imenik in ga izpiše po
abecednem vrstnem redu ključev.
"""
def izpisi_urejeno(imenik):
    kljuci = sorted(list(imenik.keys()))
    for kljuc in kljuci:
        print(f"{kljuc}: {imenik[kljuc]}")