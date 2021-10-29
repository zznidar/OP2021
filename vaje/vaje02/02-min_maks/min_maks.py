# Cim manj if-stavkov
# Za posamezno vrednost lahko pridemo do Q - 1, kjer je Q stevilo unikatnih vnosov

s = set()
for i in range(3):
    m = M = int(input(f"Vpišite {i+1}. število: "))
    s.add(m)

s = s - set([m])

for st in s:
    if st >= M:
        M = st
    elif st <= m:
        m = st

print(f"Minimum: {m}, Maksimum: {M}")