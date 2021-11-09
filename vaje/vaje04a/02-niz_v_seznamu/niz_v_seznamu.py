seznam = ["beseda", "spremenljivka", "niz", "zanka", "stavek", "slovar"]
niz = str(input("Vpišite iskani niz: "))

print(f"Seznam vsebuje niz \"{niz}\"." if (niz in seznam) else f"Seznam ne vsebuje niza \"{niz}\".")