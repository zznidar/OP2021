# uid: (ime, nivo znanja, spol)
plesalci = {0: ('Erik', 12, 'm'), 1: ('Teja', 11, 'ž'), 2: ('Urška', 6, 'ž'), 3: ('Gašper', 9, 'm'), 4: ('Sabina', 1, 'ž'), 5: ('Lucija', 3, 'ž'), 6: ('David', 3, 'm'), 7: ('Blaž', 1, 'm'), 8: ('Kaja', 3, 'ž')}

def par(prvi, drugi, erlaubt):
    # identifikacijska številka, ime, nivo znanja, spol
    if(prvi[3] != drugi[3] and abs(prvi[2] - drugi[2]) <= erlaubt):
        return((prvi[0], drugi[0]) if prvi[0] < drugi[0] else (drugi[0], prvi[0]))

def vsi_pari(plesalci, erlaubt):
    out = set()
    p = list(plesalci.items())
    for i in range(len(p)):
        for let_i in p[i+1:]:
            parus = par([p[i][0], *p[i][1]], [let_i[0], *let_i[1]], erlaubt) # ker znotraj terke ne moremo spreadati, pac naredimo list :shrug:
            if(parus):
                out.add(parus)
    return(out)

def brez_para(plesalci, erlaubt):
    imaPar = set()
    vsi = set(plesalci.keys())
    p = list(plesalci.items())
    for i in range(len(p)):
        for let_i in p[i+1:]:
            parus = par([p[i][0], *p[i][1]], [let_i[0], *let_i[1]], erlaubt) # ker znotraj terke ne moremo spreadati, pac naredimo list :shrug:
            if(parus):
                imaPar.add(p[i][0])
                imaPar.add(let_i[0])
    return(vsi - imaPar)

def zmage_na_plesalca(zmage):
    out = {}
    for par, z in zmage.items():
        i, j = par
        out[i] = (out.get(i, 0) + z)
        out[j] = (out.get(j, 0) + z)
    return(out)

plesalci = {0: ['Erik', 12, 'm'], 1: ['Teja', 11, 'ž'], 2: ['Urška', 6, 'ž'], 3: ['Gašper', 9, 'm'], 4: ['Sabina', 1, 'ž'], 5: ['Lucija', 3, 'ž'], 6: ['David', 3, 'm'], 7: ['Blaž', 1, 'm'], 8: ['Kaja', 3, 'ž']}
zmage = {(0, 1): 0, (2, 7): 3, (4, 7): 0, (1, 3): 0, (4, 6): 0, (5, 6): 0, (7, 8): 2, (5, 7): 4, (3, 5): 0, (1, 7): 0, (3, 8): 0, (2, 6): 0, (0, 5): 0, (0, 4): 1, (2, 3): 3, (1, 6): 3, (0, 8): 4, (3, 4): 1, (0, 2): 4, (6, 8): 3}
def najvec_zmag(plesalci, zmage, spol = None):
    status = zmage_na_plesalca(zmage)
    out = set()
    M = -1
    if(spol):
        plesalci = dict(filter(lambda clovek: clovek[1][2] == spol, plesalci.items()))
    for k, v in status.items():
        if(k in plesalci):
            if(v == M):
                out.add(k)
            elif(v > M):
                out = {k}
                M = v
    return(out)

## Srecno novo leto :)