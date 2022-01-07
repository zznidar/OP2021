from math import log, log10, log2
import matplotlib.pyplot as plt

"""
Napiši program, ki nariše logaritemske funkcije
(log2, log10, log) na intervalu od 0 do 5
"""

X = range(1,5001)#range(0,5.001, 0.001)
XX = []
Y_2 = []#log2(X)
Y_10 = []#log10(X)
Y_e = []#log(X)

for x in X:
    XX.append(x/1000)
    Y_2.append(log2(x/1000))
    Y_10.append(log10(x/1000))
    Y_e.append(log(x/1000))

plt.plot(XX, Y_2, label="log_2(x)")
plt.plot(XX, Y_10, label="log_10(x)")
plt.plot(XX, Y_e, label="log_e(x)")
plt.legend()
plt.show()



