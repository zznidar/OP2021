stanje = 0
while (stanje > -100):
    stanje += int(input("Sprememba: "))
    print(f"Stanje: {stanje}")
else:
    print("Bankrot!")