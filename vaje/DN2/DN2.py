ST_IGRALCEV = 2
igralci = {}
i = 0

for j in range(ST_IGRALCEV):
    igralci[j] = {"n": 0, "c": 0}

while True:
    met = int(input(f"{i+1}. igralec: "))
    if(not(1 <= met <= 6)):
        print("Vnesite veljaven rezultat!")
        continue
    igralci[i]["n"] += 1
    if(met == 6):
        igralci[i]["c"] += 1
        if(igralci[i]["c"] == 3):
            print(f"Zmagal je {i+1}. igralec.")
            print(f"Št. metov: {igralci[i]['n']}")
            break
        continue
    igralci[i]["c"] = 0
    i = (i+1)%ST_IGRALCEV