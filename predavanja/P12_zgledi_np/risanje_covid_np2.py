import matplotlib.pyplot as plt
import numpy as np

podatki = np.genfromtxt("stats.csv",
                        encoding="utf8",
                        dtype='str',
                        delimiter=",")

glava = podatki[0,:]
podatki = podatki[1:,:] # od prve vrstice naprej

datumi=podatki[:,1]

# vzamemo ven teste (4), pozitivne (6) in smrti (34)
podatki = podatki[:,[4,6,34]]
podatki[podatki=='']='0'
podatki = podatki.astype(int)


plt.plot(podatki)
plt.legend(glava[[4,6,34]])
#plt.legend([glava[4], glava[6], glava[34]])

plt.xticks(range(0,len(datumi),30),
           datumi[::30])

plt.show()


