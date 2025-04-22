# Software Benchmarking - Matrix Multiplication

Objective: 
    Establish and understand baseline performance metrics for matrix operations. 
                C[n x n] = A[n x n] x B[n x n]
    - Implement matrix multiplication in Python using NumPy and nested loops. 
    - Measure CPU performance and run tests for vector dimensions 1k, 2k, 10k, and loop counts of 1, 100, 1k, 10k, and 100k. 
    - Extend the benchmarking to GPU using CuPy or PyTorch.
    - Compare execution times between CPU and GPU. 
    - Record data for both integer and floating-point matrix operations. 

Deliverable:
    Performance table and analysis comparing CPU and optimal GPU performance. 

Purpose: 
    This step is designed to show the performance benefit of hardware accelerators like GPUs. The result will inform the later stages of the project as we scale to more complex operations. 