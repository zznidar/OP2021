def fibonaccijeva_stevila(n):
    if(n < 2):
        return([])
    st = [1, 1]
    a = 2
    while True:
        a = st[-2] + st[-1]
        if(a < n):
            st.append(a)
        else:
            break
    return(st)

def liha_fibonaccijeva_stevila(n):
    return(sum(filter(lambda x: x%2, fibonaccijeva_stevila(n))))