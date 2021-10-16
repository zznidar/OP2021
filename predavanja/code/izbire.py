"""
Program uporabniku ponudi 3 opcije:
a) pozdrav
b) racunanje ITM
c) sestevanje dveh stevil
"""

navodilo = """Izberite eno od treh opcij:
a) pozdrav
b) racunanje ITM
c) sestevanje dveh stevil
"""


izbira = input(navodilo)[0]

if izbira == "a":
    print("lep pozdrav")
elif izbira == "b":
    print("za izracun ITM preverite formulo na Wikipediji")
elif izbira == "c":
    print("Uporabite svincnik in papirus.")
else:
    raise Exception("Izbrali ste izbiro, ki ni na izbiro.")