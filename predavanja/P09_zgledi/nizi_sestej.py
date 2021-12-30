"""
Napiši funkcijo sestej_niz, ki vrne
vsoto števil, ki jih je uporabnik
naštel v nizu – števila mora uporabnik 
med seboj ločiti s presledki, decimalke
pa mora zapisati s pikami.

Kaj pa če bi bile decimalke lahko
zapisane z vejicami?
"""
def sestej(niz):
    #niz = niz.split() # s presledki
    niz = niz.split(",") # z vejicami
    niz = map(float, niz)
    return(sum(niz))

print(sestej("1,2,3,5.6"))