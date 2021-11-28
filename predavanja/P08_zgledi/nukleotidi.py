"""
Napiši funkcijo preštej, ki kot argument prejme niz, ki vsebuje sekvenco
nukleotidov. Funkcija naj vrne slovar, v katerem ključi predstavljajo
posamezen nukleotid, vrednosti pa število njegovih ponovitev.
"""
def prestej(a):
    pass
    # fn here

"""
Napiši funkcijo najbolj_pogost, ki kot argument prejme niz, ki vsebuje sekvenco
nukleotidov. Funkcija naj vrne nukleotid, ki se pojavi največkrat.
Dodatek: v primeru, da se največkrat pojavi več različnih nukleotidov,
naj funkcija vrne seznam teh.
"""
def najbolj_pogost(niz):
    naj_crke = []
    naj_ponovitev = -1
    slovar = prestej(niz)

    for crka in slovar:
        ponovitev = slovar[crka]
        if ponovitev == naj_ponovitev:
            naj_crke.append(crka)
        elif ponovitev > naj_ponovitev:
            naj_ponovitev = ponovitev
            naj_crke = [crka]
