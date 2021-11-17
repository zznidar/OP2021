# Lahko se posluzimo trika, kot ga uporablja JuliaLang za racunanje fakultet: look-up table :p

DEBUG = False

def prinz(*rest):
    """debug printing"""
    if(DEBUG):
        print(*rest)

def eratosten3(limit):
    if(limit < 3):
        return(0)

    # True: stevilo smo ze obdelali
    # False: do tega stevila se nismo prisli; lahko je prastevilo
    glavni = [True, False] * ((limit-1)//2) # nase stevilo ne rabi biti na seznamu, ker nas zanima st. prastevil do izkljucno podanega st.
    # s stevilkami: 2, 3, 4, 5 (where limit = 5): [True, False, True, False] => stevilo je index + 2
    # Still, nas seznam je lahko daljsi, ker na koncu gledamo samo do (limit-1)-2 (limita ne gledamo) (index je za 2 manjsi)

    ## Pripravimo seznam za prastevila
    prastevila = [2]
    ## Ce bo timeoutalo, naredimo samo stevcek, koliko je prastevil

    ## Poglejmo, do kod moramo loopati
    finish = ((limit-1)**0.5)-2+1 # ker nas zanima velikost indexa
    prinz("Popolnost diamanta: ", finish)

    i = 1 # ker vemo, da je 2 prastevilo, zacnemo pri 3 (index 1)
    while(i < finish):
        if not glavni[i]:
            # Prvic smo prisli do tega stevila
            # To je prastevilo.
            prastevila.append(i+2)
            # V JuliaLang bi tu element-wise mnozili matrike:
                # glavni bi bila ravno kontra: [False, True ...]
                # mnozil bi jo s [False, True, True ...]
                # Tako bi veckratniki stevila 3 postali False ("ze obiskani"), preostala stevila pa nespremenjena
                # glavni .* [false, true, true ...]
                # Julia bi sla brrrr
            # Ampak delamo v Pythonu. Too bad.
            # Probably bi bilo to mozno, ce importam numpy
            # np.array([1,2,3]) * np.array([4,5,6]) = [4,10,18]

            # Back on track
            for let_i in range(i, len(glavni), (i+2)):
                glavni[let_i] = True
        i += 1
    # Vsa glavna stevila oznacimo kot prastevila.
    prinz("Konec zanke", i, glavni, prastevila)
    # Ampak, ker smo smart, samo od trenutnega indeksa naprej *roll salfe meme*
    for let_i in range(i, limit-1-2+1):
        prinz(let_i)
        if not glavni[let_i]:
            prastevila.append(let_i+2)
    prinz(prastevila)
    return(len(prastevila))


stevilo = int(input("Vpiši število: "))
print(eratosten3(stevilo))
