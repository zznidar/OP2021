def v_cm(d, T):
    if T > 0:
        return d * 1
    elif T > -30:
        return d * (-0.3 * T + 1)
    else:
        return d * 10


def v_visine(s):
    s2 = []
    for d, tip, k, T in s:
        if tip == 's':
            k = v_cm(k, T)
        s2.append((d, tip, k, T))
    return s2


def sneg_v_mesecu(s, m=None):
    K = 0
    for d, tip, k, T in s:
        mes = int(d.split('/')[1])
        if (tip == 's'):
            if not m or (mes == m):
                K += k
    return K


def naj_padavin(s):
    naj_kolicina = 0
    naj_datumi = set()

    for d, _, k, _ in s:
        if k > naj_kolicina:
            naj_kolicina = k
            naj_datumi = {d}
        elif k == naj_kolicina:
            naj_datumi.add(d)

    return naj_datumi
