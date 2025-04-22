import cupy as cp
import matplotlib.pyplot as plt
import pandas as pd
import time
import os

sizes  = [1, 10, 100, 500, 1000, 2000, 2500, 5000, 10000, 15000, 20000]
times = []

for n in sizes:
    A = cp.random.randint(0, 100, size=(n, n))
    B = cp.random.randint(0, 100, size=(n, n))

    start = time.time()
    C = cp.dot(A, B)                        # Dot product of A and B
    cp.cuda.Device().synchronize()          # Waiting for GPU to finish
    end = time.time()

    duration = end - start
    times.append(duration)
    print(f"n={n} | Time taken: {end - start: .4f} seconds")

data = {
    'Matrix Size (n x n)': sizes,
    'Time Taken (seconds)': times
}

df = pd.DataFrame(data)
excel_path = r"C:\Prabhav\Prabhav HP\Prabhav Projects & Courses\Hardware-Accelerator-for-FFT\Software Benchmarking - Matrix Multiplication\cupy_int_matrix_mult.xlsx"

with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='MatrixMultTiming')

# Plot the results
plt.plot(sizes, times, marker='o', linestyle='-', color='blue')
plt.xlabel('Matrix Size (n x n)')
plt.ylabel('Time Taken (seconds)')
plt.title('Matrix Multiplication Performance (CuPy)')
plt.grid(True)
plt.tight_layout()

# Save to same folder as script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "cupy_int_matrix_mult_result.png")
plt.savefig(output_path, dpi=300)

plt.show()