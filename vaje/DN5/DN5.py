import pandas as pd
def preberi_podatke(path):
    return(pd.read_csv(path, sep=";"))

def vrni_povprecja_po_krajih(df):
    return(df.mean())

def vrni_dneve_najvisje_onesnazenosti(df):
    return(df.idxmax()+1)

def brez_manjkajocih_meritev(df):
    return(set(df.dropna(axis=1).columns))