
"""
Napiši funkcijo odstrani_podniz,
ki kot argument sprejme dva niza in iz
prvega niza odstrani prvo pojavitev
drugega niza.
"""
def odstrani_podniz(niz1, niz2):
    return(niz1.replace(niz2, "", 1))

    for i in range(len(niz1) - len(niz2) + 1):
        rez = niz1[i:i+len(niz2)]
        if rez == niz2:
            idx1 = i
            idx2 = i+len(niz2)
            return(niz1[:idx1] + niz1[idx2:])
