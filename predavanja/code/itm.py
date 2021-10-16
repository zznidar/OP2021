"""
Program, ki prebere telesno maso in visino
in izracuna indeks telesne mase (ITM)
"""

def itm(m, h):
    return(m//h**2)

itmL = lambda m, h: check(m/h**2)
##js: itmL = (m, h) => (m/h**2)

def check(itm):
    if(itm < 18.5):
        return(itm, "Masa premajhna")
    elif(itm > 25):
        return(itm, "Masa prevelika")
    else:
        return(itm, "Ustrezna masa.")

m = float(input("Vnesi telesno maso [kg]: "))
h = float(input("Vnesi višino [cm]: "))/100

print(itmL(m, h))