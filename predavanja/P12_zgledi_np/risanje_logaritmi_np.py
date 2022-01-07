import matplotlib.pyplot as plt
import numpy as np

"""
Napiši program, ki nariše logaritemske funkcije
(log2, log10, log) na intervalu od 0 do 5
"""

#X = np.arange(0.001,5.001, 0.001)
X = np.linspace(0.001, 5, 1000)
Y_2 = np.log2(X)
Y_10 = np.log10(X)
Y_e = np.log(X)

plt.plot(X, Y_2, label="log_2(x)")
plt.plot(X, Y_10, label="log_10(x)")
plt.plot(X, Y_e, label="log_e(x)")
plt.legend()
plt.show()



