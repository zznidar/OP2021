def minimum(s):
    """Vrni najmanjsi element podanega seznama.

    :param s: vhodni seznam
    :return: najmanjsi element seznama
    """
    if len(s) == 0: 
        raise ValueError("s should not be an empty list")
    
    m = s[0]
    for let_i in s:
        if let_i < m:
            m = let_i
    return(m)

def trikotniska_neenakost(a, b, c):
    """Vrni, ali lahko s podanimi dolzinami stranic tvorimo trikotnik.

    :param a: stranica a
    :param b: stranica b
    :param c: stranica c
    :return: bool, ali velja trikotniska neenakost
    """
    return(a + b > c and a + c > b and b + c > a)

def samoglasnik(s):
    """Preveri, ali je dani znak samoglasnik.
    
    :param s: znak
    :return: bool, ali je samoglasnik
    """
    SAMOGLASNIKI = ["a", "e", "i", "o", "u"]
    return(s.lower() in SAMOGLASNIKI)

def pH(c):
    """Vrni vrednost pH.
    
    :param c: molarna koncentracija oksonijevih ionov [M]
    :return: vrednost pH
    """

    from math import log10
    return(-log10(c))

def prekrivajoca_seznama(s1, s2):
    """Preveri, ali imata seznama vsaj en skupen element.

    :param s1: prvi seznam
    :param s2: drugi seznam
    :return: bool, ali se seznama prekrivata
    """
    # V bistvu bi tu lahko dodali se *rest, kar bi omogocilo preverjanje neomejenega stevila seznamov.
    # Ampak bi bilo treba kodo malce spremeniti.
    return(bool(set(s1) & set(s2)))