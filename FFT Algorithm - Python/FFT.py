# FFT.py
import cmath

'''
Compute the discrete Fourier transform of list `samples` via Cooley–Tuk recursion.
'''

def FFT(samples):
    # Find the number of samples we have
    # FFT only works efficiently when n is a power of two
    n = len(samples)

    # Execute the end of the recursive even/odd splits once we only have one sample
    # If n == 1, the DFT of a single point is just the point itself
    if n == 1:
        return samples[:]      # Return a copy
    
    # Split the samples into even and odd subsums. Find half the total number of samples.
    m = n // 2
    x_even = [samples[2*i] for i in range(m)]
    x_odd = [samples[2*i + 1] for i in range(m)]

    # Perform the recursive FFT operation on the odd and even sides 
    # Each returns a list of length m representing the DFTs of the even- and odd-subsequences.   
    f_even  = FFT(x_even)
    f_odd   = FFT(x_odd)

    # Combine the values found
    result = [0] * n

    for k in range(m):
        # For each split set, we need to multiple a k-dependent complex number by the odd subsum
        # Compute the "twiddle factor", then assemble the full transform of the length n
        W_nk                = cmath.exp(-2j * cmath.pi * k / n)
        result[k]           = f_even[k] + (W_nk * f_odd[k])
        result[k + m]       = f_even[k] - (W_nk * f_odd[k])
        
    return result