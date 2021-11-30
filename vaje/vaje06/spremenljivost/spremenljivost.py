def koreni_seznam(seznam):
    for let_i in range(len(seznam)):
        if(seznam[let_i] >= 0):
            seznam[let_i] **= 0.5
        else:
            seznam[let_i] = None

def koreni_seznam2(seznam):
    out = []
    for s in seznam:
        out.append(s**0.5 if s >= 0 else None)
    return(out)

def unikaten_seznam(seznam):
    unikaten = []
    for s in seznam:
        if s not in unikaten:
            unikaten.append(s)
    return(unikaten)