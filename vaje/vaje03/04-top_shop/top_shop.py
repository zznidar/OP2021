vsota = 0
i = 0

while True:
    cena = int(input("Cena artikla: ")) 
    if cena == 0:
        break
    vsota += cena
print(f"Vsota: {vsota}")