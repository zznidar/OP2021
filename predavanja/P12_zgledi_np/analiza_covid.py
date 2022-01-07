import numpy as np

"""
Pred casom smo ze uporabljali funkcijo, ki je uvozila podatke
o okuzbah po regijah
"""
from uvozi_podatke2 import uvozi_regije
regije = uvozi_regije()

# najprej pretvorimo regije v ndarray
sez = []
for ime,podatki in regije:
    sez.append(podatki)

matrika = np.array(sez)

# potem lahko izracunamo povprecje po vseh podatkih
print("Povprecje vseh", np.mean(matrika))


# povprecje po datumih
print("Povprecje po datumih",
      np.mean(matrika, axis=0))

# povprecje po krajih
print("Povprecje po krajih",
      np.mean(matrika, axis=1))
