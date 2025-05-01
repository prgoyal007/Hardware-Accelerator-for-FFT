'''
def IFFT(p):
    # P - [P(w^0), P(w^1), ..., P(w^(n-1))] value representation 
    n = len(p)  # n is a power of 2
    if n == 1:
        return p
    
    w = e^((2* pi * i) / n)

    P_e, P_o = P[::2], P[1::2]
    y_e, y_o = FFT(P_e), FFT(P_o)

    y = [0] * n

    for j in range(n/2):
        y[j] = y_e[j] + (w^j * y_o[j])
        y[j + n/2] = y_e[j] - (w^j * y_o[j])

    return y
'''