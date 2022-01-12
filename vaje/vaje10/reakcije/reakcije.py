import matplotlib.pyplot as plt

def kemijski_sistem(k1, k_1):
    THRESHOLD = 0.00001
    s1 = 0 # nM
    ds1 = k1 - k_1*s1
    while(ds1 > THRESHOLD):
        s1 += ds1
        ds1 = k1 - k_1*s1
    return(s1)

def izris(k1, k_1):
    data = [0]
    THRESHOLD = 0.00001
    s1 = 0 # nM
    ds1 = k1 - k_1*s1
    while(ds1 > THRESHOLD):
        s1 += ds1
        data.append(s1)
        ds1 = k1 - k_1*s1
    plt.plot(data)
    plt.show()

def kemijski_sistem_dva(k1, k_1, k2, k_2, k3, k_3):
    THRESHOLD = 0.00001
    s1 = s2 = 0
    ds1 = k1 + k3*s2 - (k_1 + k_3)*s1
    ds2 = k2 + k_3*s1 - (k_2 + k3)*s2
    while(abs(ds1) > THRESHOLD or abs(ds2) > THRESHOLD):
        s1 += ds1
        s2 += ds2
        ds1 = k1 + k3*s2 - (k_1 + k_3)*s1
        ds2 = k2 + k_3*s1 - (k_2 + k3)*s2
    return((s1, s2))

def izris_dva(k1, k_1, k2, k_2, k3, k_3):
    data = [[0], [0]]
    THRESHOLD = 0.00001
    s1 = s2 = 0
    ds1 = k1 + k3*s2 - (k_1 + k_3)*s1
    ds2 = k2 + k_3*s1 - (k_2 + k3)*s2
    while(abs(ds1) > THRESHOLD or abs(ds2) > THRESHOLD):
        s1 += ds1
        s2 += ds2
        data[0].append(s1)
        data[1].append(s2)
        ds1 = k1 + k3*s2 - (k_1 + k_3)*s1
        ds2 = k2 + k_3*s1 - (k_2 + k3)*s2
    plt.plot(data[0])
    plt.plot(data[1])
    plt.legend(["$S_1$", "$S_2$"])
    plt.show()

def kemijski_sistem_tri(k1, k_1, k2, k_2, k3, k_3, k4, q):
    THRESHOLD = 0.00001
    s1 = s2 = 0
    ds1 = k1 + k3*s2 - (k_1 + k_3)*s1
    ds2 = k2/(1 + k4*(s1**q)) + k_3*s1 - (k_2 + k3)*s2
    while(abs(ds1) >= THRESHOLD or abs(ds2) >= THRESHOLD):
        s1 += ds1
        s2 += ds2
        ds1 = k1 + k3*s2 - (k_1 + k_3)*s1
        ds2 = k2/(1 + k4*(s1**q)) + k_3*s1 - (k_2 + k3)*s2
    return((s1, s2))

def izris_tri(k1, k_1, k2, k_2, k3, k_3, k4, q):
    data = [[0], [0]]
    THRESHOLD = 0.00001
    s1 = s2 = 0
    ds1 = k1 + k3*s2 - (k_1 + k_3)*s1
    ds2 = k2/(1 + k4*(s1**q)) + k_3*s1 - (k_2 + k3)*s2
    while(abs(ds1) >= THRESHOLD or abs(ds2) >= THRESHOLD):
        s1 += ds1
        s2 += ds2
        data[0].append(s1)
        data[1].append(s2)
        ds1 = k1 + k3*s2 - (k_1 + k_3)*s1
        ds2 = k2/(1 + k4*(s1**q)) + k_3*s1 - (k_2 + k3)*s2
    plt.plot(data[0])
    plt.plot(data[1])
    plt.legend(["$S_1$", "$S_2$"])
    plt.show()