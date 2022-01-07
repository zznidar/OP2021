import matplotlib.pyplot as plt
from uvozi_podatke import uvozi_podatke
import numpy as np

datumi, testi, pozitivni, smrti = uvozi_podatke("stats.csv")

datumi = np.array(datumi)
testi = np.array(testi)
pozitivni = np.array(pozitivni)
smrti = np.array(smrti)

"""
datumi=datumi[-150:]
testi=testi[-150:]
pozitivni=pozitivni[-150:]
smrti=smrti[-150:]
"""
plt.plot(datumi,testi, label="testov", color="green")
plt.plot(datumi,pozitivni, label="pozitivnih", color="red")
plt.plot(datumi,smrti, marker='.',
         linestyle='', markersize=1,
         label="smrti", color='black')

indeksi_nad = pozitivni > np.mean(pozitivni)
pozitivni_nad = pozitivni[indeksi_nad]
datumi_nad = datumi[indeksi_nad]

plt.plot(datumi_nad,
         pozitivni_nad,
         marker='x',
         linestyle='',
         markersize=10,
         color="black")



plt.legend()



plt.title("COVID-19 v Sloveniji")
plt.xlabel("dan")
plt.ylabel("število primerov")

plt.xticks(range(0,len(datumi),30), datumi[::30])


plt.show()

"""
datumi, testi, pozitivni, smrti, smrti_sk = uvozi_podatke("data_small.csv")


plt.plot(datumi, testi, '.', markersize=5, color="#fdbb84", label="Testov")
plt.plot(datumi, pozitivni, '.', markersize=5, color="red", label="Pozitivni")
plt.plot(datumi, smrti, color="black", label="Smrti")
plt.plot(datumi, smrti_sk, color="grey", label="Smrti (skupno)")

# označi osi x in y
plt.xlabel("Dan")
plt.ylabel("Število")

# označi naslov
plt.title("COVID-19 v Sloveniji")

# prikaži legendo z oznakami
plt.legend()

# prikaži samo določene oznake pod osjo x
# prikažemo vsak 10. datum
plt.xticks(range(0, len(datumi), 20), datumi[::20])

# prikaži graf
plt.show()

# samo za december
datumi_12 = []
testi_12 = []
pozitivni_12 = []

"""

"""
d12 = []
t12 = []
p12 = []

for d, t, p in zip(datumi, testi, pozitivni):
    leto, mesec, dan = d.split("-")
    if leto == "2021" and mesec == "12":
        d12.append(dan+"."+mesec+".")
        t12.append(t)
        p12.append(p)


loc1=[]
loc2=[]
for i in range(len(d12)):
    loc1.append(i-0.2)
    loc2.append(i+0.2)

plt.bar(loc1, t12, width = 0.4)
plt.bar(loc2, p12, width = 0.4)
plt.xticks(range(len(d12)), d12)


plt.xlabel("dan")
plt.ylabel("primeri")

plt.show()
"""
"""
for d, t, p in zip(datumi, testi, pozitivni):
    mesec = d.split("/")[1]
    if mesec == "12":
        datumi_12.append(d)
        testi_12.append(t)
        pozitivni_12.append(p)


#plt.plot(datumi_12, testi_12)
#plt.plot(datumi_12, pozitivni_12)
#plt.show()

loc1 = []
loc2 = []
for i in range(len(datumi_12)):
    loc1.append(i-0.2)
    loc2.append(i+0.2)


plt.bar(loc1, pozitivni_12, width=0.4)
plt.bar(loc2, testi_12, width=0.4)
plt.legend(["pozitivni", "testi"])
plt.xticks(range(0,len(datumi_12),2), datumi_12[::2])

plt.xlabel("Dan")
plt.ylabel("Primeri")

plt.show()


"""
