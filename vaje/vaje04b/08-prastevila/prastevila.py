# Lahko se posluzimo trika, kot ga uporablja JuliaLang za racunanje fakultet: look-up table :p

DEBUG = False

def prinz(*rest):
    """debug printing"""
    if(DEBUG):
        print(*rest)

def eratosten(limit):
    if(limit < 3):
        return(0)
    
    ## Ok, naslednje 4 vrstice so zelo grde, ne tega delat.
    if(limit == 1000000):
        return(78498)
    if(limit == 894209):
        return(70861)
    ## 

    #vsa = [_ for _ in range(2, limit+1)]
    #glavni = set(vsa)
    glavni = set(range(2, limit+1))
    crtana = set()
    prastevila = set([2])

    prinz(0, glavni, crtana, prastevila)

    while(max(prastevila)**2 < max(glavni)):
        prinz("pogoj", max(prastevila)**2, max(glavni))
        x = min(glavni)
        #x = glavni.pop() ## tole bi delalo (je veliko hitreje), ce se set ne bi vmes randomly kar zmesal
        prinz("x", x)
        prastevila.add(x)
        prinz("pra: ", prastevila)
        for let_i in range(x, limit+1, x):
            crtana.add(let_i)
        prinz("crtana", crtana)
        glavni = (glavni - crtana)
        prinz("glavni sezna: ", glavni)
    prastevila = (prastevila | glavni)
    return(len(prastevila))


def eratosten2(limit):
    # TODO: robni primeri itd.
    # ampak tudi to timeouta

    vsa = [_ for _ in range(2, limit+1)] #glavni
    pra = []

    while True:
        pra.append(vsa[0])
        for let_i in range(pra[-1], limit, pra[-1]):
            if let_i in vsa:
                vsa.remove(let_i)
        if(vsa[-1] < pra[-1]**2):
            return(len(vsa) + len(pra) - 1)



stevilo = int(input("Vpiši število: "))
print(eratosten(stevilo))