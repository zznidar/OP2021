serije = [
    ('Friends', 9.0, 1994),
    ('The Big Bang Theory', 8.4, 2007),
    ('Game of Thrones', 9.5, 2011),
    ('Mr. Robot', 8.7, 2015),
    ('Humans', 8.1, 2015),
]

def ocene(serije):
    ok = []
    for title, rating, year in serije:
        if rating >= 9:
            ok.append(title)
    return(ok)

def najstarejsa(serije):
    o_title, o_year = None, None
    ## drugi del pogoja OR se ne izvrsi, ce je prvi True,
    ## zato nimamo tezav int < None
    for title, rating, year in serije:
        if not o_year or year < o_year:
            o_title, o_year = title, year
    return(o_title)

def povprecna_ocena(serije):
    vsota = 0
    for _, rating, _ in serije:
        vsota += rating
    avg = vsota/(len(serije) or 1)
    return(round(avg, 2))

def dolga_imena(serije):
    out = []
    for title, _, _ in serije:
        if(len(title.split(" ")) > 2):
            out.append(title)
    return(out)

def krajsanje(serije):
    out = []
    for title, rating, _ in serije:
        out.append((title, rating))
    return(out)

def najnovejse(serije):
    out = []
    n_year = None
    for title, _, year in serije:
        if not n_year or year == n_year:
            out.append(title)
            n_year = year
        elif year > n_year:
            out = [title]
            n_year = year
    return(out)
