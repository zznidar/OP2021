izdelki = [
    ('mleko', 0.86, 128),
    ('jogurt', 0.49, 56),
    ('piškoti', 2.99, 73),
    ('sok', 1.79, 104),
    ('jajce', 0.1, 103),
    ('moka', 1.39, 99),
    ('makaroni', 1.89, 67),
    ('paradižnik', 0.23, 35),
    ('kruh', 2.19, 43),
    ('hrenovka', 1.99, 28),
    ('gorgonzola', 2.69, 32)
]
# (izdelek, cena, zaloga)

""" def v_slovar(izdelki):
    out = {}
    for ime, *rest in izdelki:
        out[ime] = rest
    return(out) """

def v_slovar(izdelki):
    return({ime: rest for ime, *rest in izdelki})

zaloga = v_slovar(izdelki)
def stevilo_izdelkov(zaloga):
    out = 0
    for _, z in zaloga.values():
        out += z
    return(out)

seznam = ['jogurt', 'mleko', 'jogurt', 'jogurt', 'piškoti']
def nakupovalna_kosara(seznam):
    out = {}
    for s in seznam:
        out[s] = out.get(s, 0) + 1
    return(out)

def cena(zaloga, slovar_nakupov):
    out = 0
    for izdelek, kolicina in slovar_nakupov.items():
        out += (zaloga[izdelek][0] * kolicina) # predpostavimo, da je vedno dovolj zaloge.
    return(out)

def popravek_zaloge(zaloga, izdelek, popravek):
    if -popravek <= zaloga[izdelek][1]:
        zaloga[izdelek][1] += popravek
        return(zaloga[izdelek][1])
    else:
        return(None)

def blagajna(zaloga, slovar_nakupov):
    for i, p in slovar_nakupov.items():
        popravek_zaloge(zaloga, i, -p)
    return(cena(zaloga, slovar_nakupov))

jedi = {
    "palačinke": {"jajce": 3, "mleko": 1, "moka": 1},
    "šmorn": {"jajce": 3, "mleko": 1, "moka": 1},
    "hrenovke": {"hrenovka": 2, "kruh": 1},
    "makaroni": {"makaroni": 1, "paradižnik": 3, "gorgonzola": 1},
    "piškoti": {"piškoti": 1}
}
def kuhanje(zaloga, jedi, jed):
    return(cena(zaloga, jedi[jed]))

def posamezna_jed(jedi, jed, obrokov):
    return({s: n*obrokov for s, n in jedi[jed].items()})

obroki = [("makaroni", 20), ("palačinke", 15), ("šmorn", 10), ("hrenovke", 5)]
def nakup(jedi, obroki):
    potreba = {}
    for j, o in obroki:
        neki = posamezna_jed(jedi, j, o)
        for s, n in neki.items():
            potreba[s] = potreba.get(s, 0) + n
    return(potreba)

def primanjkljaj(zaloga, jedi, obroki):
    # prevec dela, bomo to enkrat drugic. Lp
    pass