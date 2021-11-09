sez = eval(input("Vpišite seznam števil: "))
m = sez[0]

for s in sez[1:]:
    if(s < m):
        m = s

print(m)