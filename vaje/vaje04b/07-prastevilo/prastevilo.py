def prastevilo(st):
    # 1 ni prastevilo
    if(st == 1):
        return(False)
        
    for let_i in range(2, st//2+1):
        if(st%let_i == 0):
            return(False)
    return(True)

stevilo = int(input("Vpiši število: "))
print(prastevilo(stevilo))