a = float(input("Vpiši a: "))
b = float(input("Vpiši b: "))
c = float(input("Vpiši c: "))

x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

if(isinstance(x1, complex)):
    # Tudi x2 je complex, upostevajoc zakon o niclah funkcij
    print("Enačba nima realnih rešitev.")
elif(x1 != x2):
    print(f"Enačba ima dve realni rešitvi: {round(x1, 4)} in {round(x2, 4)} ")
else:
    print(f"Enačba ima eno realno rešitev: {round(x1, 4)} ")
