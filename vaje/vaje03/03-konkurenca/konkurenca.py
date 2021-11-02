no_of_articles = int(input("Število izdelkov: "))
vsota = 0

i = 0

while i < no_of_articles:
    vsota += int(input("Cena artikla: "))
    i += 1
print(f"Vsota: {vsota}")