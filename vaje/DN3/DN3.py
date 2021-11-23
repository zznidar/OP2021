def pretvori_v_sekunde(cas):
    time = (f"0:0:0:{(cas or 0)}").split(":")
    (h, m, s) = time[-3:]
    print(h, m, s)

    dolzina = int(s) + int(m)*60 + int(h)*3600

    return(dolzina)

def vrni_skupno_dolzino(posnetki):
    test = map(pretvori_v_sekunde, posnetki)
    #print(test)
    skupna = sum(test)
    return(skupna)

def vrni_povprecno_dolzino(posnetki):
    povprecna = vrni_skupno_dolzino(posnetki)/(len(posnetki) or 1)
    return(round(povprecna))


""" def je_krajsa(cas, limit):
    return(cas <= limit)
 """

def vrni_krajse(posnetki, M):
    limit = pretvori_v_sekunde(M)
    krajsi = list(filter(lambda cas: pretvori_v_sekunde(cas) <= limit, posnetki))
    #print(krajsi)
    return(krajsi)
