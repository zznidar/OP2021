"""
napisi funkcijo ITM, ki sprejme
dve imeni datotek. Iz prve datoteke
naj prebere podatke o osebah,
izracuna njihov ITM in tega skupaj
z imenom osebe shrani v drugo datoteko
"""

def ITM(ime1, ime2):
    f1 = open(ime1, encoding="utf8")
    f2 = open(ime2, 'w', encoding="utf8")
    print("ime;ITM", file=f2)

    f1.readline() # preskočim prvo vrstico, ki je drugačna od ostalih

    for vrstica in f1:
        vrstica=vrstica.strip()
        ime, visina, teza = vrstica.split(";")
        visina = float(visina)/100
        teza = float(teza)
        itm = teza/(visina**2)
        print(ime, itm, sep=";", file=f2)

    f1.close()
    f2.close()
        
