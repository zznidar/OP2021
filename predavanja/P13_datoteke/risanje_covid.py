from uvozi_podatke import uvozi_podatke
import matplotlib.pyplot as plt

datumi, testi, pozitivni, smrti = uvozi_podatke("stats.csv")


#datumi = datumi[-100:]
#testi = testi[-100:]
#pozitivni = pozitivni[-100:]
#smrti = smrti[-100:]


plt.plot(datumi,
         testi,
         color='blue',
         label = "testi") # št. testov
plt.plot(datumi,
         pozitivni,
         color='red',
         label="pozitivni")
plt.plot(datumi,
         smrti,
         marker=".",
         linestyle = "",
         color='black',
         label="smrti")

plt.xlabel("Datum")
plt.ylabel("Število primerov")
plt.title("COVID v Sloveniji")
plt.legend()

lokacije_oznak = range(0,len(datumi),30)
oznake = datumi[::30]

for i in range(len(oznake)):
    leto, mesec, dan = oznake[i].split("-")
    oznake[i] = leto + "-" + mesec

plt.xticks(lokacije_oznak, oznake)


plt.savefig("covid.png")
plt.show()
