a = float(input("Vpiši dolžino prve katete: "))
b = float(input("Vpiši dolžino druge katete: "))

c = (a**2 + b**2)**0.5

S = 0.5*a*b

print(f"Dolžina hipotenuze: {round(c, 2)}")
print(f"Ploščina trikotnika: {round(S, 2)}")