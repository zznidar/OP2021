C = float(input("Vpiši temperaturo [°C]: "))
enota = input("Želite pretvoriti v Kelvine (vpiši K) ali Fahrenheite (vpiši F)? ")

if enota == "K":
    rezultat = C + 273.15
    print(f"{C} °C je enako {rezultat} K")
elif enota == "F":
    rezultat = C * 9/5 + 32
    print(f"{C} °C je enako {rezultat} °F")
else:
    print("Vnesli ste napačno enoto!")
