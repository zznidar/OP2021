# tole kodo bomo podrobneje spoznali na koncu semestra
# zaenkrat je tule samo zato, da nam priskrbi podatke
# če želite imeti današnje podatke, boste morali namestiti knjižnico pandas: pip install pandas

def uvozi_podatke():
    try:
        import pandas as pd
        url = 'https://raw.githubusercontent.com/sledilnik/data/master/csv/stats.csv' # pot do podatkov
        df = pd.read_csv(url) # branje podatkov
        oktober_2021 = df.loc[df['date'].str.startswith("2021-10"), ['date', 'tests.positive', 'tests.performed']].dropna() # samo oktober 2021
        datumi = list(oktober_2021['date'].astype(str))
        pozitivni = list(oktober_2021['tests.positive'].astype(int))
        delez_pozitivnih = list((100*oktober_2021['tests.positive']/oktober_2021['tests.performed']).round(2))

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


    
