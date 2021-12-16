"""
Izberi si ustrezno podatkovno strukturo za beleženje prijateljstev
med množico izbranih ljudi in z njo predstavi omrežje prijateljstev.

Pri tem upoštevaj, da želimo nad strukturo izvajati sledeče operacije:
- dodajanje prijateljev
- brisanje prijateljev
- iskanje skupnih prijateljev
- iskanje osebe z največ prijatelji
- ...
"""

## Lahko bi imeli set urejenih terk
prijatelji = {("oseba1", "oseba2"), ("oseba1", "oseba3")} # where terka je abecedno urejena
# Sam iz tega težko iščeš skupne prijatelje.


"""
Napiši funkcijo prijatelji_od, ki izpiše vse prijatelje podane osebe.
"""

def prijatelji_od(prijatelji, ime):
    if ime in prijatelji:
        return(prijatelji[ime])



"""
Napiši funkcijo spoprijatelji, ki kot argument prejme dve osebi in ju
spoprijatelji. Če sta osebi že v prijateljstvu, naj funkcija to izpiše.
"""
def spoprijatelji(prijatelji, ime1, ime2):
    dodaj_osebe(prijatelji, ime1, ime2)
    prijatelji[ime1].add(ime2)
    prijatelji[ime2].add(ime1)
    # Slovar je spremenljiv, zato ni treba ničesar returnati.

"""
Dodaj še funkcijo dodaj_osebo, ki v primeru, da podana oseba še ne obstaja,
le-to med opazovane ljudi doda.
"""
def dodaj_osebo(prijatelji, ime):
    if ime not in prijatelji:
        prijatelji[ime] = set()

def dodaj_osebe(prijatelji, *rest):
    for r in rest:
        dodaj_osebo(prijatelji, r)

"""
Napiši funkcijo skregaj, ki kot argument prejme dve osebi in ju
"odprijatelji". Če osebi nista v prijateljstvu, naj funkcija to izpiše.
"""
def skregaj(prijatelji, ime1, ime2):
    if ime1 not in prijatelji and ime2 not in prijatelji:
        print("Osebi ne obstajata")
        return
    if ime2 not in prijatelji[ime1]:
        print("Osebi nista prijatelja.")
        return
    prijatelji[ime1].discard(ime2)
    prijatelji[ime2].discard(ime1)

"""
Napiši funkcijo generiraj_omrezje, ki kot argument sprejme seznam ljudi,
vrne pa naključno omrežje prijateljstev (uporabi funkcijo sample modula random).
"""
from random import sample
def generiraj_omrezje(osebe):
    prijatelji = {} # prazno omrezje
    for i in range(len(osebe)):
        ime1, ime2 = sample(osebe, 2)
        spoprijatelji(prijatelji, ime1, ime2)
    return(prijatelji)

"""
Napiši funkciji, ki ugotovita, kdo ima največ in kdo najmanj prijateljev.
Kaj pa če ima več oseb enako veliko oziroma enako malo prijateljev?
"""
def najvec(prijatelji):
    # isto kot imdb
    for k, v in prijatelji:
        pass
    pass

"""
Napiši funkcijo skupni, ki kot argument sprejme dve osebi in vrne njune
skupne prijatelje.
"""
# presek
def skupni(prijatelji, ime1, ime2):
    if ime1 not in prijatelji or ime2 not in prijatelji:
        return(set())
    return(prijatelji[ime1] & prijatelji[ime2])

"""
Napiši funkcijo brez_njegovih, ki kot argument sprejme dve osebi in vrne
prijatelje, ki so prijatelji prve osebe, niso pa prijatelji druge osebe.
"""
# razlika
def brez_njegovih(prijatelji, ime1, ime2):
    if ime1 not in prijatelji:
        return(set())
    if ime2 not in prijatelji:
        return(prijatelji[ime1])
    return(prijatelji[ime1] - prijatelji[ime2])

# unija
def vsaj_od_enega(prijatelji, ime1, ime2):
    dodaj_osebe(prijatelji, ime1, ime2) # da se ne matraš v vsaki fn
    return(prijatelji[ime1] | prijatelji[ime2])

"""
Napiši funkcijo, ki izpiše vse prijatelje prijateljev podane osebe.

Dodatki:
- posamezno osebo naj izpiše le enkrat;
- iz izpisa naj izpusti podano osebo;
- v izpis naj vključi samo tiste osebe, ki niso neposredni prijatelji
    od opazovane osebe;
-izpis naj uredi po abecednem vrstnem redu.
"""

"""
Poišči par(e), ki ima(jo) največ skupnih prijateljev
"""
