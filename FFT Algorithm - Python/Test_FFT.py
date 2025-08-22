# Test_FFT.py
'''
To Test Functionality of Custom FFT vs NumPy's FFT:

RUN in Terminal @current directory: 
python -m pytest -q        
'''

import pytest
import numpy as np
from FFT import FFT

# Helper: compare two complex numbers (or floats) within tolerance
def almost_equal(a, b, tol=1e-6):
    return abs(a - b) < tol

@pytest.mark.parametrize("x, expected", [
    # 1) constant signal -> only DC term nonzero
    ([1, 1, 1, 1], [4, 0, 0, 0]),
    # 2) simple [1, 0, -1, 0] test case
    ([1, 0, -1, 0], np.fft.fft([1, 0, -1, 0])),
])

# Test small signals with known outputs or against NumPy directly.
def test_known_signals(x, expected):
    F = FFT(x)

    # If expected is a NumPy array, cast to list for indexing
    for i in range(len(x)):
        assert almost_equal(F[i], expected[i]), f"Mismatch at bin {i}"

# Compare custom FFT to numpy.fft.fft on random real inputs
def test_random_signals():
    random = np.random.RandomState(0)
    
    for n in (8, 16, 32):
        x   = random.randn(n).tolist()

        F_my = FFT(x)
        F_np = np.fft.fft(x)

        for i in range(n):
            assert almost_equal(F_my[i], F_np[i]), (
                f"Random test failed for n = {n} at index {i}: "
                f"{F_my[i]} != {F_np[i]}"
            )

'''
import numpy as np
from FFT import FFT

def almost_equal(a, b, tol=1e-6):
    return abs(a - b) < tol

def test_known_signals():
    cases = [
        ([1,1,1,1], [4,0,0,0]),
        ([1,0,-1,0], np.fft.fft([1,0,-1,0])),
    ]
    for x, expected in cases:
        F = FFT(x)
        for i in range(len(x)):
            assert almost_equal(F[i], expected[i]), f"{x=} → bin {i}: {F[i]} != {expected[i]}"

def test_random_signals():
    rng = np.random.RandomState(0)
    for n in (8,16,32):
        x = rng.randn(n).tolist()
        F_my = FFT(x); F_np = np.fft.fft(x)
        for i in range(n):
            assert almost_equal(F_my[i], F_np[i]), f"n={n} idx={i}: {F_my[i]} != {F_np[i]}"

if __name__ == "__main__":
    print("Running tests…")
    test_known_signals()
    test_random_signals()
    print("All tests passed!")
'''