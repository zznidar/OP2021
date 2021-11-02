vsota = 0
i = 0

while True:
    cena = int(input("Cena artikla: ")) 
    if cena == 0:
        break
    vsota += cena
    i += 1

print(f"Vsota: {vsota}")
print(f"Povprečna cena: {round(vsota/(i or 1), 5)}")