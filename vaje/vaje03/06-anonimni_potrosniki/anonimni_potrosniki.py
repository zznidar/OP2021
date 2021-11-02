vsota = 0
i = 0

while (i < 10 and vsota < 100):
    cena = int(input("Cena: ")) 
    if cena == 0:
        break
    vsota += cena
    i += 1

print(f"Porabili boste {vsota} evrov za {i} stvari.")
