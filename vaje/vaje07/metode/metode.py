def aa_besede(s):
    s = s.replace(".", "").split()
    out = set()
    for el in s:
        if el.lower().count("a") >= 2:
            out.add(el)
    return(out)

def najdaljse_besede(s):
    s = s.replace(".", "").replace(",", "").split()
    out, l = set(), 0
    for el in s:
        if len(el) == l:
            out.add(el)
        elif len(el) > l:
            l = len(el)
            out = {el}
    return(out)

def velike_zacetnice(s):
    L = 2 #const
    out = []
    for el in s.split():
        if len(el) > 2:
            out.append(f"{el[0].upper()}{el[1:]}")
        else:
            out.append(el)
    return(" ".join(out))

def razlicne_skladbe(seznam):
    return(len(set(seznam)))

def skupne(seznam1, seznam2):
    # presek
    return(set(seznam1) & set(seznam2))

def repertuar(seznam1, seznam2):
    # repertoar
    # unija
    return(set(seznam1) | set(seznam2))

def unikatna_predvajanja(seznam1, seznam2):
    # XOR
    return(set(seznam1) ^ set(seznam2))

from collections import Counter
def ponavljajoci_znaki(niz):
    # from collections import Counter, sam on vrne dict
    return(set(filter(lambda x: x[1] > 1, Counter(niz).items())))

def najveckrat_onesnazena_mesta(data, kraji):
    # (dan, (Ljubljana, Maribor, Celje))
    out = set()
    const_M = 50
    
    counter = [0]*len(kraji)
    for dan, postaje in data:
        for p in range(len(postaje)):
            if((postaje[p] or -1) >= const_M):
                counter[p] += 1
    M = 1
    for c in range(len(counter)):
        if counter[c] == M:
            out.add(kraji[c])
        elif counter[c] > M:
            out = {kraji[c]}
            M = counter[c]
    return(out)