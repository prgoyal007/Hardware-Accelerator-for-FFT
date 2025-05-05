# Phase 1: Software Benchmarking - Matrix Multiplication
# Purpose and Objective
The primary goal of this phase was to establish baseline performance metrics for matrix multiplication on the CPU and GPU. Since matrix multiplication is a fundamental operation in many computational tasks—including FFT and other signal processing workloads—understanding its behavior in both software and hardware contexts is critical. This benchmarking serves as a reference point for evaluating the potential speedups and efficiency gains offered by a hardware accelerator later in the project.

Specifically, this phase explores how execution time varies:
- Between CPU and GPU implementations. 
- Between integer-based and floating-point matrices. 
- Across different matrix sizes.

These comparisons help highlight the computational trade-offs involved in data representation and hardware utilization.

# Structure of the Python Files
To isolate and analyze each of these variables independently, the benchmarking was divided across four separate Python scripts:
NumPy_Int_Matrix_Mult.py    -    Performs matrix multiplication on the CPU using NumPy with integer matrices.
NumPy_Float_Matrix_Mult.py    -    Performs matrix multiplication on the CPU using NumPy with floating-point matrices.
CuPy_Int_Matrix_Mult.py    -    Performs matrix multiplication on the GPU using CuPy with integer matrices.
CuPy_Float_Matrix_Mult.py    -    Performs matrix multiplication on the GPU using CuPy with floating-point matrices.

Separating the tests ensures clarity, modularity, and reproducibility, and allows each result set to be evaluated and graphed independently.

# Comparison of NumPy vs CuPy (CPU vs GPU)
By comparing NumPy (which executes operations on the CPU) and CuPy (which uses the GPU), the benchmarking illustrates the performance differential between general-purpose processors and specialized hardware. The key goals were:
- To quantify the acceleration factor offered by GPU computing.
- To determine how GPU performance scales with matrix size.
- To understand whether GPU acceleration is more beneficial for certain data types or workloads.

This comparison is particularly relevant when transitioning to hardware acceleration, as it gives context on whether a custom-designed accelerator is likely to compete with GPU performance.

# Comparison of Integer vs Floating-Point Operations 
Integer and floating-point operations differ in terms of:
- Computation complexity
- Hardware resource requirements
- Precision and accuracy

This benchmarking phase investigates whether:
- Floating-point matrices introduce a significant performance penalty,
- Integer operations are more efficient on the CPU/GPU,
- The data type has an impact on how well the GPU accelerates the task.

These results inform decisions about whether the hardware FFT implementation should target integer or fixed-point arithmetic instead of full floating-point logic, which can be more costly in hardware.

# Graph and Table Outputs
Each Python script outputs:
- A table showing execution times (in seconds or milliseconds) for various matrix sizes (e.g., 512×512, 1024×1024, 2048×2048).
- A graph (line plot or bar chart) comparing runtime as matrix size increases.
- These visualizations provide a clear representation of scalability, showing:
- How well each platform handles increasing computational load,
- Whether the GPU advantage grows with matrix size,
- How integer vs floating-point operations impact performance over scale.

# Summary of Insights
- GPU (CuPy) significantly outperforms CPU (NumPy) at large matrix sizes, particularly for floating-point operations.
- Integer operations are typically faster than floating-point on both platforms, but floating-point is essential for many signal processing tasks, including FFT.
- The trade-off between speed and numerical precision is a key consideration for hardware design.
- These benchmarks establish a performance baseline that the upcoming Verilog-based FFT accelerator will be measured against.
