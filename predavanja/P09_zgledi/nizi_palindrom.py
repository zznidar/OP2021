"""
Napiši funkcijo palindrom, ki vrne True,
če je podan niz palindrom, sicer pa vrne False.
Pri tem naj ignorira presledke, male in velike
črke.
"""

def palindrom(niz):
    #if niz == niz[::-1]
    niz = niz.lower()
    niz = niz.replace(" ", "")

    i = 0
    while i < len(niz)//2:
        if niz[i] != niz[-1-i]:
            return False
        i += 1
    return True