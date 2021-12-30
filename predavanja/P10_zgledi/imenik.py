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
def poisci(imenik, ime):
    if ime in imenik:
        return imenik[ime]
    return False


"""
Napiši funkcijo dodaj, ki kot argument sprejme imenik, ime osebe
in njeno telefonsko številko. Funkcija vnos doda v imenik le v primeru,
da oseba v imeniku še ne obstaja. Sicer naj izpiše, da oseba že obstaja.
"""
def dodaj(imenik, ime, stevilka):
    if ime not in imenik:
        imenik[ime] = stevilka
    else:
        print("Oseba že obstaja")
"""
Zgled: Napiši funkcijo popravi, ki kot argument sprejme imenik, ime osebe
in njeno telefonsko številko. Funkcija spremeni telefonsko številko le
v primeru, da oseba v imeniku že obstaja.
"""
def popravi(imenik, ime, stevilka):
    if ime in imenik:
        imenik[ime] = stevilka
    else:
        print("Oseba še ne obstaja")

"""
Zgled: Napiši funkcijo izbrisi, ki kot argument sprejme imenik in ime osebe.
Če oseba v imeniku obstaja, naj jo funkcija izbriše, sicer naj javi, da te
osebe ni v imeniku.
"""
def izbrisi(imenik, ime):
    if ime in imenik:
        del imenik[ime]
    else:
        print("Osebe ni v imeniku")

"""
Zgled: Napiši funkcijo izpisi_slovar,
ki kot argument sprejme imenik in tega
izpise po vrsticah v obliki ime osebe: telefonska stevilka.
"""
def izpisi(imenik):
    for ime, st in imenik.items():
        print(ime, ":", st)

"""
Napiši funkcijo izpisi_urejeno, ki kot
argument sprejme imenik in ga izpiše po
abecednem vrstnem redu ključev.
"""
def izpisi_urejeno(imenik):
    kljuci = sorted(list(imenik.keys()))
    for kljuc in kljuci:
        print(kljuc, ":", imenik[kljuc])
   

"""
Napiši funkcijo, ki iz datoteke s podanim
imenom ustvari slovar, ki vsebuje telefonski 
imenik. Predpostavljaj, da ima datoteka strukturo,
kot jo prikazuje primer v datoteki imenik.txt. 
Funkcija naj vrne prebran slovar.
Dodatek: funkcija naj deluje tudi za datoteke, 
ki lahko vsebujejo vmes
prazne vrstice (glej imenik1.txt)
"""

    
"""
Zgled: Napiši funkcijo shrani_imenik, ki shrani 
telefonski imenik (zapisan v obliki slovarja) v 
podano datoteko. Vsak vnos v imeniku naj bo 
zapisan v svoji vrstici, ime in telefonska številka 
pa naj bosta ločena z vejico. 
"""

