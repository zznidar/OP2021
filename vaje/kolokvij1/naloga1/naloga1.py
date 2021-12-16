#def check(sneg, temperatura):
#    if(sneg >= 50 and temperatura < -2):
#        return(True)
#    else:
#        return(False)

def checks(sneg):
    if(sneg >= 50):
        return(True)
    else:
        return(False)

def checkt(temperatura):
    if(temperatura < -2):
        return(True)
    else:
        return(False)

sums, sumt = 0, 0
dni = 0

while True:
    ## Kolk pogresam javascript, kjer lahko reces v stilu
    ## if(checks(s = float(input("neki neki"))) && checkt(t = float...))
    ## in ti spotoma nastavi var na to vrednost :)
    
    s = float(input("Vnesi dnevno količino snega [cm]: "))
    if(not checks(s)):
        break
    t = float(input("Vnesi povprečno dnevno temperaturo [°C]: "))
    if(not checkt(t)):
        break
    dni += 1
    sums += s
    sumt += t

if(dni == 0):
    print("Lažen preplah!")
else:
    print(f"Čas trajanja izrednih razmer (v dnevih): {dni}")
    print(f"V tem času je zapadlo {round(sums, 2)} cm snega.")
    print(f"Povprečna dnevna temperatura je bila {round(sumt/(dni or 0), 2)} °C.")


