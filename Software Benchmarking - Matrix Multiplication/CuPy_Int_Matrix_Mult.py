import cupy as cp
import matplotlib.pyplot as plt
import time

sizes  = [1, 10, 100, 500, 1000, 2000, 2500, 5000, 10000, 15000, 20000, 25000]
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

# Plot the results
plt.plot(sizes, times, marker='o', linestyle='-', color='blue')
plt.xlabel('Matrix Size (n x n)')
plt.ylabel('Time Taken (seconds)')
plt.title('Matrix Multiplication Performance (Cuda)')
plt.grid(True)
plt.tight_layout()
plt.savefig("cuda_matrix_mult_result.png", dpi=300)
plt.show()