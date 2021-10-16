"""
Prebere niz in izpise,
ali niz vsebuje sumevce
"""

SUMEVCI = ["č", "š", "ž"]

def preveri(niz):
    for s in SUMEVCI:
        if(s in niz.lower()):
            return("Vsebuje vsaj en sumevec.")
    return("Ne vbsebuje sumevca.")
        

niz = input("Vnesi niz: ")
print(preveri(niz))