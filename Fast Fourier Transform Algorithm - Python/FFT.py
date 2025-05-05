import math
"""
C++ Code for FFT

vector<complex<double>> FFT(vector<complex<double>> &samples) {

    // Find the number of samples we have
    int N = samples.size();

    // Execute the end of the recursive even/odd splits once we only have one sample
    if (N == 1) {
        return samples;
    }

    // Split the samples into even and odd subsums. Find half the total number of samples.
    int M = N / 2;

    // Declare an even and an odd complex vector
    vector<complex<double>> Xeven(M, 0);
    vector<complex<double>> Xodd(M, 0);

    // Input the even and odd samples into respective vectors
    for (int i=0; i != M; i++){
        Xeven[i] = samples[2*i];
        Xodd[i] = samples[2*i + 1];
    }

    // Perform the recursive FFT operation on the odd and even sides
    vector<complex<double>> Feven(M, 0);
    Feven = FFT(Xeven);
    vector<complex<double>> Fodd(M, 0);
    Fodd = FFT(Xodd);

    /*----------------- END RECURSION --------------------- */
    // Declare vector of frequency bins
    vector<complex<double>> freqbins(N, 0);

    // Combine the values found
    for (int k = 0; k != N/2; k++) {
        // For each split set, we need to multiply a k-dependent complex
        // number by the odd subsum
        complex<double> cmplx_exp = polar(1.0, -2*pi*k/N) * Fodd[k];
        freqbins[k] = Feven[k] + cmplx_exp;

        //Everytime you add pi, exponential changes sign
        freqbins[k+N/2] = Feven[k] - cmplx_exp;
    }

return freqbins;
}


"""
'''
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