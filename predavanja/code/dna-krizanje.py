niz1 = input("Vnesi prvi niz: ")
niz2 = input("Vnesi drugi niz: ")

niz12 = niz1[:len(niz1)//2] + niz2[len(niz2)//2:]
niz21 = niz2[:len(niz2)//2] + niz1[len(niz1)//2:]

print(f"Križanec 1: {niz21}")
print(f"Križanec 2: {niz12}")
