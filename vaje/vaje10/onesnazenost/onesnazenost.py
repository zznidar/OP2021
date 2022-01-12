import numpy as np
import matplotlib.pyplot as plt


# matplotlib: za risanje grafov (avtomatizacija, da se ne ukvarjas z Excelom) // Tega ne bo na kolkviju :upside_down:
#   plt.show() prikaze in hkrati izbrise plot. Treba znova .plot(x, y)

# numpy: poenostavi delo (npr. branje podatkov iz datoteke)

## array = polje; vsi elementi so istega podatkovnega tipa. Operacije se izvajajo paralelno na vseh elementih hkrati.
## vecdimenzionalnost; a.shape: 6 vrstic po 2 stolpca; a.size: st. elementov; a.ndim = stevilo dimenzij
# a.reshape((3,2,2))
# Lazje indeksiranje a[1,0]
# vecdimenzionalni slajsi: a[:,1] = 1. stolpec vseh vrstic

# np.nanmin(a): ignorira NaN-e 

def preberi_podatke(datoteka):
    #a = np.genfromtxt(datoteka, delimiter=";", names=True, dtype="int")
    #return(a)

    f = open(datoteka, "r", encoding="utf8")
    kraji = f.readline().strip().split(";")
    a = np.genfromtxt(datoteka, delimiter=";", skip_header=True, dtype="int")
    return(a, kraji)
preberi_podatke('podatki/januar.csv')

podatki, _ = preberi_podatke('podatki/januar.csv')
def povprecje(podatki):
    return(np.average(podatki))

def povprecje_po_dnevih(podatki):
    return(np.average(podatki, axis=1))

def povprecje_po_krajih(podatki):
    return(np.average(podatki, axis=0))

podatki, kraji = preberi_podatke('podatki/januar.csv')
def shrani_graf(podatki, napisi):
    FILENAME = "onesnazenost.png"
    plt.plot(podatki)
    plt.legend(napisi)
    #plt.show()
    plt.savefig(FILENAME)