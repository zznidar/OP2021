def check(sez, n):
    M = max(sez)
    for f in range(1, int(M/(n or 1)) + 1):
        if(n*f in sez):
            return("Vsebuje.")
    return("Ne vsebuje.")

# Ker max() jamra, ce je seznam prazen
sez = (eval(input("Vpišite seznam števil: ")) or [0])
n = float(input("Vnesite število: "))

print(check(sez, n))