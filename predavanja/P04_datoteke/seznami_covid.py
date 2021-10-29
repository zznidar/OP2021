# uvozi podatke
from uvozi_covid import uvozi_podatke
datumi, pozitivni, delez_pozitivnih, datumi_pozitivni, pozitivni_datumi = uvozi_podatke()

"""
Od tu naprej so naloge s seznami
"""

## Dostopanje do elementov

# Koliko pozitivnih je bilo prvi dan, koliko zadnji dan?
pozitivni[0]
pozitivni[-1]

# Seznam lahko tudi spreminjamo... 
pozitivni[-1] += 10

## Funkcije nad seznami
min(pozitivni)
max(pozitivni)

# Kakšno je bilo povprečno število pozitivnih? Kaj pa minimalno in maksimalno? Koliko dni imamo na voljo?
avg = sum(pozitivni)/len(pozitivni)

## Operatorji nad seznami

# Ali je bilo kdaj točno 1000 pozitivnih primerov?

# Brisanje zadnjega dne?
del pozitivni[-1]

## Metode seznamov

# Sortiranje. Največ primerov, najmanj primerov. 
pozitivni.sort(reverse=True)

# Mediana?
pozitivni.sort()
if(pozitivni):
    if(len(pozitivni)%2 == 1):
        # srednji element
        i = len(pozitivni)//2
        mediana = pozitivni[i]
    else:
        # aritmeticna sredina srednjih dveh elementov
        i = len(pozitivni)//2
        mediana = (pozitivni[i-1] + pozitivni[i])/2

# Dan, ko je bilo največ primerov. Dan, ko je bilo najmanj primerov.

## Rezine

# Rezine: prvi trije, zadnji trije? Vsi razen prvih treh in zadnjih treh...

# prva in druga polovica meseca

# vsak drugi dan

# petki, sobote, nedelje

## Zanke

# Izpis števila pozitivnih po vrsticah (brez in z datumom).







