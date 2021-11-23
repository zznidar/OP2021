def prastevilo(n):
    if(n == 1):
        return(False)
    for let_i in range(2, n):
        if not(n%let_i):
            return(False)
    return(True)

def prastevila(n):
    pra = []
    for let_i in range(2, n+1):
        if(prastevilo(let_i)):
            pra.append(let_i)
    return(pra)

def deljivost(n, x):
    kolikokrat = 0
    while(n % x == 0):
        kolikokrat += 1
        n /= x
    return(kolikokrat)

def razcep_na_prafaktorje(n):
    prafaktorji = []
    for let_i in prastevila(n):
        d = deljivost(n, let_i)
        if(d):
            prafaktorji.append([let_i, d])
    return(prafaktorji)