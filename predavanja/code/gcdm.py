import math # Za olajsanje mnozenja lista na koncu

def presek(prafaktorji):
    # prafaktorji je dictionary prafaktorjev za vsak input
    faktorji = list(prafaktorji.values())[0]
    # Itak rabimo samo prvega pregledovati, ker GCD
    #print(faktorji)
    # za vsak element prvega lista pogledamo vse ostale
    # ce je ujemanje, ga popnemo; ce je v obeh, zapisemo v output

    skupni = []
    while len(faktorji) > 0:
        f = faktorji[0] # ker odstranimo ujemajoci se element (tudi iz prvega lista), vedno gledamo samo prvi element
        skip = False
        for stevilo, praf in prafaktorji.items():
            if f in praf:
                prafaktorji[stevilo].remove(f)
                # odstranis ta element
            else:
                skip = True
                break # ne gledamo naprej
        if skip:
            continue
        # Prisli smo skozi vse, vsi ga vsebujejo
        # Zdej pa dejansko dodamo.
        skupni.append(f)
        #print(skupni)
    #print("Skupni: ", skupni)
    return(skupni)


def GCDm(st): 
    # st Array
    prafaktorji = {} # dictionary arrajev
    for s in st:
        prafaktorji[s] = [1]
        # dobimo prafaktroje
        i = 2
        dejanskiS = s # Key v dictionaryju, ker se _s_ spreminja
        while(s != 1):
            if(s % i == 0):
                # je deljiv
                prafaktorji[dejanskiS].append(i)
                s /= i
            else:
                i += 1

    ## Opomba: tu bi lahko loopali samo do i,
    ## ki je 0.5 * s (ali celo do sqrt(s))
    ##; na koncu loopa avtomatsko recemo,
    ## da je prafaktor kar stevilo s

    skupni = presek(prafaktorji)

    ## Izpisemo rezultat, sam ga moramo najprej zmnoziti
    rezultat = math.prod(skupni)
    print(rezultat)


#GCDm([1, 2, 3, 4])
#GCDm([100, 20, 30, 40])
#GCDm([100000000, 200000000, 300000000])
#GCDm([7919, 7907])

ARR = list(map(int, input("Vnesi stevila, locena s presledkom, za izracun GCD: ").split()))
print(ARR)
GCDm(ARR)