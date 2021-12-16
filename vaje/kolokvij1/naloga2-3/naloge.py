def v_cm(padavine, T):
    k = (1 if T >= 0 else (1-0.3*T) if -30 < T < 0 else 10) # grda koda, :notes: pam param pam pam :notes:
    h = padavine * k
    return(h)

def v_visine(data):
    # data = [(datum, tip_padavin, kolicina_padavin, temperatura), ...]
    out = []
    for datum, tip_padavin, kolicina_padavin, temperatura in data:
        if(tip_padavin == "s"):
            out.append((datum, tip_padavin, v_cm(kolicina_padavin, temperatura), temperatura))
        else:
            out.append((datum, tip_padavin, kolicina_padavin, temperatura))
    return(out)

def sneg_v_mesecu(data, month = None):
    ## manjkajo vejice: sprejme seznam terk, kot ga vrača Naloga 2b*vejica* in številko meseca*vejica* zapisano kot int*vejica* in vrne skupno
    sums = 0
    for datum, tip_padavin, kolicina_padavin, temperatura in data:
        if(not month or int(datum.split("/")[1]) == month):
            ## Spet pogresam js, ki zna primerjati str == int :upside_down:
            sums += kolicina_padavin if tip_padavin == "s" else 0
    return(sums)

def naj_padavin(data):
    out = set()
    M = 0
    for datum, tip_padavin, kolicina_padavin, temperatura in data:
        if(kolicina_padavin == 0):
            continue
        if(kolicina_padavin == M):
            out.add(datum)
        elif(kolicina_padavin > M):
            out = {datum}
            M = kolicina_padavin
    return(out)