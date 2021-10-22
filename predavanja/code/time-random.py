"""
Izpise 2 random stevili [10, 100]
in stopa, koliko casa uporabnik racuna.
"""

from time import perf_counter
from random import randint

a, b = randint(10, 100), randint(10, 100)

t1 = perf_counter()
print(f"Koliko je {a} + {b}?")

vnos = int(input("Vnesi rezultat: "))
while vnos != a+b:
    vnos = int(input("Nope. Vnesi rezultat: "))
t2 = perf_counter()
print(f"Porabil si {round(t2 - t1, 2)} sekund.")