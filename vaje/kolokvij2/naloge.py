def v_seznam(path):
    f = open(path, "r", encoding="utf8")
    f.readline() # header
    out = []
    #(vpisna, ime, priimek, predmet, ocena) src
    #(vpisna, priimek, ime, predmet, ocena) out
    for vrstica in f:
        vrstica = vrstica.strip()
        #print(vrstica)
        if(not vrstica):
            #print("prazna")
            continue
        if(vrstica[0] == "#"):
            #print("Comment")
            continue
        vpisna, ime, priimek, predmet, ocena = vrstica.split(";")
        out.append((vpisna, priimek, ime, predmet, int(ocena)))
    f.close()
    return(out)

def v_slovarja(data):
    """vrne terko z dvema slovarjema"""
    lookup = {}
    redovalnica = {}
    for vpisna, priimek, ime, predmet, ocena in data:
        lookup.setdefault(vpisna, (priimek, ime))
        redovalnica.setdefault(vpisna, []).append((predmet, ocena))
    return((lookup, redovalnica))


def manjkajoci(data, predmeti=None):
    vsi_predmeti = set(predmeti or [])
    koncani = {}
    out = {}
    for vpisna, priimek, ime, predmet, ocena in data:
        if(not predmeti):
            vsi_predmeti.add(predmet)
        koncani.setdefault(vpisna, set()).update([predmet] if ocena > 5 else [])
    for k, v in koncani.items():
        out[k] = vsi_predmeti - v
    return(out)