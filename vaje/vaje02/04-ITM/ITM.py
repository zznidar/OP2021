h = float(input("Telesna višina [cm]: "))/100
m = float(input("Teža [kg]: "))

itm = m/(h**2)

print(f"Vaš indeks telesne mase je: {round(itm, 2)}")

if(itm < 18.5):
    print("Pojejte kakšen kos torte več! ;)")
elif(itm > 25):
    print("Treba se bo več gibati in jesti bolj zdravo!")
else:
    print("Super, nadaljujte s svojim življenjskim stilom!")