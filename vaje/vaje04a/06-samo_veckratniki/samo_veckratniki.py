## Zelimo vedeti, ali so vsi elementi veckratniki tega stevila.

def check(sez, n):
    for s in sez:
        if s%n:
            return("Ne vsebuje.")
    return("Vsebuje.")

# Ker max() jamra, ce je seznam prazen
sez = (eval(input("Vpišite seznam števil: ")) or [0])
n = float(input("Vnesite število: "))

print(check(sez, n))