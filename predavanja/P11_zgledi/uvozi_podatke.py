"""
Napiši funkcijo uvozi_podatke, ki kot argument sprejme ime datoteke.
Na podlagi podane datoteke zgenerira in vrne terko sledečih seznamov:
- datum
- število (int) testov na dan
- število (int) pozitivnih testov na dan
- kumulativno število (int) smrti
"""

def pretvori(x):
    return(int(x) if x else 0)

def razlika(S):
    # koliko je novih med prvim in drugim elementom seznama.
    ## Ker imamo samo kumulativne podatke
    D = [S[0]]
    for i in range(1, len(S)):
        d = S[i] - S[i-1]
        D.append(d)
    return(D)

def uvozi_podatke(ime):
    f = open(ime, encoding="utf8")
    f.readline() # odstranimo prvo vrstico 
    
    datumi = []
    testi = []
    pozitivni = []
    smrti_sk = []
    smrti = []
    
    for vrstica in f:
        vrstica = vrstica.strip() # odstranimo whitespace
        seznam = vrstica.split(",")
        d, t, p, s_Sk = seznam # razpakiramo

        t = pretvori(t)
        p = pretvori(p)
        s_sk = pretvori(s_sk)

        datumi.append(d)
        testi.append(t)
        pozitivni.append(p)
        smrti_sk.append(s_sk)

    smrti = razlika(smrti_sk)
    
    return(datumi, testi, pozitivni, smrti, smrti_sk)
        
















def v_stevilo(niz):
    if niz == "":
        return 0
    
    return int(niz)

def uvozi_podatke(ime):
    f = open(ime, encoding="utf8")

    datumi = []
    testi = []
    pozitivni = []
    smrti = []


    x = f.readline()
    """
    s = x.split(",")
    print(s.index('date'))
    print(s.index('tests.performed'))
    print(s.index('tests.positive'))
    print(s.index('state.deceased.todate'))
    """

    
    for vrstica in f:
        vrstica=vrstica.strip()
        seznam = vrstica.split(",")
        datum = seznam[1]
        t = seznam[4]
        p = seznam[6]
        s = seznam[34]
        
        datumi.append(datum)
        testi.append(v_stevilo(t))
        pozitivni.append(v_stevilo(p))
        smrti.append(v_stevilo(s))

    f.close()    

    return datumi[:-1], testi[:-1], pozitivni[:-1], smrti[:-1]

    
