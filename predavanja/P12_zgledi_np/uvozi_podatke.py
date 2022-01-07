"""
Napiši funkcijo uvozi_podatke, ki kot argument sprejme ime datoteke.
Na podlagi podane datoteke zgenerira in vrne terko sledečih seznamov:
- datum
- število (int) testov na dan
- število (int) pozitivnih testov na dan
- kumulativno število (int) smrti
"""
def v_st(x):
    if x != "":
        return int(x)
    else:
        return 0

def uvozi_podatke(ime):
    f = open(ime, encoding="utf8")
    #x = f.readline().strip().split(",")
    #print(x.index("tests.performed"))
    #print(x.index("tests.positive"))
    #print(x.index("state.deceased.todate"))

    f.readline()

    datumi = []
    testi = []
    pozitivni = []
    smrti_skupaj = []

    for vrstica in f:
        vrstica=vrstica.strip()
        sez = vrstica.split(",")
        datum = sez[1]
        testov = v_st(sez[4])
        pozitivnih = v_st(sez[6])
        smrti = v_st(sez[34])

        datumi.append(datum)
        testi.append(testov)
        pozitivni.append(pozitivnih)
        smrti_skupaj.append(smrti)
        
    return datumi, testi, pozitivni, smrti_skupaj
  
