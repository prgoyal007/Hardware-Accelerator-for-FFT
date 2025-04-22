import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import os

sizes  = [1, 10, 100, 500, 1000, 1500, 1750, 2000]
times = []

for n in sizes:
    A = np.random.randint(0, 100, size=(n, n))
    B = np.random.randint(0, 100, size=(n, n))

    start = time.time()
    C = np.dot(A, B)
    end = time.time()

    duration = end - start
    times.append(duration)
    print(f"n={n} | Time taken: {duration: .4f} seconds")

data = {
    'Matrix Size (n x n)': sizes,
    'Time Taken (seconds)': times
}

df = pd.DataFrame(data)
excel_path = r"C:\Prabhav\Prabhav HP\Prabhav Projects & Courses\Hardware-Accelerator-for-FFT\Software Benchmarking - Matrix Multiplication\numpy_int_matrix_mult.xlsx"

with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='MatrixMultTiming')

# Plot the results
plt.plot(sizes, times, marker='o', linestyle='-', color='blue')
plt.xlabel('Matrix Size (n x n)')
plt.ylabel('Time Taken (seconds)')
plt.title('Integer-Point Matrix Multiplication Performance (NumPy)')
plt.grid(True)
plt.tight_layout()

# Save to same folder as script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "numpy_int_matrix_mult_result.png")
plt.savefig(output_path, dpi=300)

plt.show()