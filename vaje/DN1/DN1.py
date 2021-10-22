pozivi = ["Vnesite število levkocitov / µl: ", 
"Vnesite delež nevtrofilcev [%]: ", 
"Vnesite število trombocitov / µl: ", 
"Vnesite nivo AST [UI/L]: ", 
"Vnesite starost pacienta [leta]: "]


def preveri(d):
    if d[0] > 13_700:
        return("nizko tveganje (N5)")
    if d[3] > 50:
        return("visoko tveganje (V3)")
    elif 35 < d[3] <= 50:
        if d[2] > 282_000:
            return("nizko tveganje (N4)")
        if d[4] > 6.75:
            return("visoko tveganje (V2)")
        else:
            return("nizko tveganje (N3)")
    if d[1] > 68:
        if d[2] > 291_000:
            return("nizko tveganje (N2)")
        else:
            return("visoko tveganje (V1)")
    else:
        return("nizko tveganje (N1)")



# Dictionary v Pythonu je ordered sele od 3.7 dalje. V izogib nedoslednosti uporabimo array.
data = []

for p in pozivi:
    data.append(float(input(p)))

print(preveri(data))

