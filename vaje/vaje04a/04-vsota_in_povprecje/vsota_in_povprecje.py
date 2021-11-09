sez = eval(input("Vpišite seznam števil: "))
vsota = 0

for s in sez:
    vsota += s
    
# just because testi niso zadovoljni z 0.0
avg = (vsota/(len(sez) or 1) or 0) 

print(vsota)
print(round(avg, 5))