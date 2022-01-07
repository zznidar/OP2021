# tole kodo bomo podrobneje spoznali na koncu semestra
# zaenkrat je tule samo zato, da nam priskrbi podatke
# če želite imeti današnje podatke, boste morali namestiti knjižnico pandas: pip install pandas

def uvozi_podatke():
    try:
        import pandas as pd
        url = 'https://raw.githubusercontent.com/sledilnik/data/master/csv/stats.csv' # pot do podatkov
        df = pd.read_csv(url) # branje podatkov
        jesen_2021 = df.loc[df['date'].str.startswith("2021-1"), ['date', 'tests.positive', 'tests.performed']].dropna() # samo jesen 2021
        datumi = list(jesen_2021['date'].astype(str))
        pozitivni = list(jesen_2021['tests.positive'].astype(int))
        delez_pozitivnih = list(jesen_2021['tests.positive']/jesen_2021['tests.performed'])

        f = open("covid.txt", mode="w", encoding="utf8")
        for d, p, delez in zip(datumi, pozitivni, delez_pozitivnih):
            print(d,p,delez, sep=";", file=f)
        f.close()
        
    except:
        datumi = []
        pozitivni = []
        delez_pozitivnih = []
        
        f = open("covid.txt", encoding="utf8")
        for l in f:
            d, p, delez = l.strip().split(";")
            p = int(p)
            delez=float(delez)

            datumi.append(d)
            pozitivni.append(p)
            delez_pozitivnih.append(delez)
           
        f.close()


    datumi_pozitivni = [[d,p] for d,p in zip(datumi, pozitivni)]
    pozitivni_datumi = [[p,d] for d,p in zip(datumi, pozitivni)]

    return datumi, pozitivni, delez_pozitivnih, datumi_pozitivni, pozitivni_datumi


def uvozi_regije(reg_filter = ["KP", "LJ", "MB"]):
    try:
        import pandas as pd
        url = 'https://raw.githubusercontent.com/sledilnik/data/master/csv/stats.csv' # pot do podatkov
        df = pd.read_csv(url)
        cols = list(df.columns[df.columns.str.startswith("region")])
        cols = cols[:-3] # remove foreign, unknown and cumulative
        cols = ['date'] + cols
        df = df[cols]

        #df = df.loc[df['date'].str.startswith("2021-1")].dropna() # samo jesen 2021

        df.drop(columns=['date'], inplace=True)

        df.columns = [x.split(".")[1].upper() for x in cols[1:]]
        df = (df-df.shift(1)).dropna() # razlika med vrsticama da število novih primerov

        primeri = df.values.astype(int).transpose().tolist()

        regije = [[r,p] for r,p in  list(zip(df.columns, primeri))]

        f = open("covid_regije.txt", mode="w", encoding="utf8")
        for r, primeri in regije:
            print(r+";" + ",".join([str(p) for p in primeri]), file=f)
            
        f.close()
        
    except:
        regije = []
        f = open("covid_regije.txt", encoding="utf8")
        for l in f:
            r, primeri = l.strip().split(";")
            primeri = [int(p) for p in primeri.split(",")]

            regije.append([r, primeri])
           
        f.close()

    if not reg_filter:
        return regije
    
    regije2 = []
    
    for r in regije:
        if r[0] in reg_filter:
            regije2.append(r)
    

    return regije2





        
