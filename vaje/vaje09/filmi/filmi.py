def preberi(datoteka):
    f = open(datoteka, "r", encoding="utf8")
    besedilo = f.read()
    f.close()
    return(besedilo)

def v_seznam(datoteka):
    out = []
    f = open(datoteka, "r", encoding="utf8")
    for v in f:
        naslov, ocena, zanr, leto = v.strip().split(';')
        out.append([naslov, float(ocena), zanr, int(leto)])
    f.close()
    return(out)

def v_slovar(datoteka):
    out = {}
    for naslov, _, zanr, _ in v_seznam(datoteka):
        # out[zanr] = (out.get(zanr, []).append(naslov)) ## for some unknown reason, tole ne dela. Neke Python-specific kaprice. V js bi to slo brrr
        out.setdefault(zanr, []).append(naslov)
    return(out)

def oblikovan_izpis(datoteka):
    print("{:25}{:4}".format("Naslov filma", "Leto"))
    print("-"*29)
    for naslov, _, _, leto in v_seznam(datoteka):
        print("{:25}{:4}".format(naslov, leto))

def najljubsi(datoteka_pisanja):
    ti = input("Najljubši film: ")
    f = open(datoteka_pisanja, "w", encoding="utf8")
    f.write(ti)
    f.close()

def zapis(datoteka_branja, datoteka_pisanja):
    with open(datoteka_pisanja, "w", encoding="utf8") as f:
        for n, _, _, _ in sorted(v_seznam(datoteka_branja)):
            f.write(f"{n}\n")
    
import pandas as pd
csv_datoteka = "podatki/ratings.csv"
def ocena_filma(id_filma, csv_datoteka):
    df = pd.read_csv(csv_datoteka, sep=",", header=None)
    df.columns=["userId", "movieId", "rating", "timestamp"]
    return( df[df["movieId"] == id_filma]["rating"].mean() ) 