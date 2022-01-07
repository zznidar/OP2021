import matplotlib.pyplot as plt
import numpy as np

podatki = np.genfromtxt("stats.csv",
                        encoding="utf8",
                        delimiter=",")

# znebimo se 0-te vrstice
podatki = podatki[1:,:] # od prve vrstice naprej

# vzamemo ven teste (4), pozitivne (6) in smrti (34)
podatki = podatki[:,[4,6,34]]
plt.plot(podatki)
plt.legend(['testi', 'pozitivni', 'smrti'])
plt.show()


