h = int(input("Vpiši višino: "))

for let_i in range(h):
    print(" " * (h-1-let_i) + "*" * (let_i*2 + 1))
