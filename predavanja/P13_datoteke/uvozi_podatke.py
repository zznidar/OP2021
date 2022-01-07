"""
Napiši funkcijo uvozi_podatke, ki kot argument sprejme ime datoteke.
Na podlagi podane datoteke zgenerira in vrne terko sledečih seznamov:
- datum
- število (int) testov na dan
- število (int) pozitivnih testov na dan
- kumulativno število (int) smrti
"""
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

    
