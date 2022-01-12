def stevilo_besed(datoteka):
    f = open(datoteka, "r", encoding="utf8")
    vsebina = f.read()
    f.close()
    ## Ocitno ni dobro samo presteti presledkov?!
    #return(vsebina.count(" ") + 1) # built-in count je najhitrejsi nacin

    return(len(vsebina.split())) # iz lanskih resitev

from collections import Counter
def razlicni_znaki(datoteka):
    f = open(datoteka, "r", encoding="utf8")
    vsebina = f.read()
    f.close()
    return(len(Counter(vsebina)))

def najpogostejsi_znak(datoteka):
    f = open(datoteka, "r", encoding="utf8")
    vsebina = f.read()
    f.close()
    vse = Counter(vsebina)
    # Markusova lambdica
    znak, pojavnost = max(vse.items(), key=lambda c: c[1])
    return(znak)

def hapax(datoteka):
    f = open(datoteka, "r", encoding="utf8")
    vsebina = f.read().split()
    f.close()
    vse = Counter(vsebina)

    enkratne = list(filter(lambda c: c[1] == 1, vse.items()))
    return(len(enkratne))