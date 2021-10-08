def GCD(a, b):
    while(a != b):
        if(a > b):
            a = a - b
        else:
            b = b - a
    print(a)

#GCD(100, 75)

## Branje podatkov
A = int(input("Vnesi stevilo A"))
B = int(input("Vnesi stevilo B"))
GCD(A, B)