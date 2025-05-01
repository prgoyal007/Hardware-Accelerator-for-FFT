import math

def FFT(p):
    n = len(p) # n is a power of 2
    if n == 1:
        return p
    
    for i in n:
        w = math.e^((2 * math.pi * i) / n)
        P_e, P_o = [], []
        y_e, y_o = FFT(P_e), FFT(P_o)

    for j in range(n/2):
        y[j] = y_e[j] + (w^j * y_o[j])
        y[j + n/2] = y_e[j] - (w^j * y_o[j])

    return y

'''
def FFT(p):
    # P - [p_0, p_1, ..., p_n-1] coeff representation 
    n = len(p)  # n is a power of 2
    if n == 1:
        return p
    
    w = e^((2* pi * i) / n)

    P_e, P_o = [p_0, p_2, ..., p_n-2], [p_1, p_3, ..., p_n-1]
    y_e, y_o = FFT(P_e), FFT(P_o)

    y = [0] * n

    for j in range(n/2):
        y[j] = y_e[j] + (w^j * y_o[j])
        y[j + n/2] = y_e[j] - (w^j * y_o[j])

    return y
'''