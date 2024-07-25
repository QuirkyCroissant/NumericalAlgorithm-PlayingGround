# Numerical Algorithm Solvers

This repository contains a collection of assignments from the 'Numerical Algorithm' course at the University of Vienna. Through three different Jupyter notebooks, we explore various techniques and algorithms to inspect numerical stability, precision, convergence, and performance for large matrices. Each assignment investigates a specific type of solver best suited for different problems.

## Project Structure

### Themes

#### LU and PLU Factorisation
In this section, we delve into LU (Lower-Upper) and PLU (Permutation-Lower-Upper) factorization techniques. These are fundamental matrix decomposition methods used to solve systems of linear equations, invert matrices, and compute determinants. The LU factorization decomposes a matrix into a product of a lower triangular matrix and an upper triangular matrix. The PLU factorization includes a permutation matrix, enhancing numerical stability.

#### Jacobi and Gauss-Seidel
This section covers the Jacobi and Gauss-Seidel iterative methods for solving linear systems. The Jacobi method is a straightforward algorithm that solves each equation in isolation, using the previous iteration's values. The Gauss-Seidel method improves upon this by immediately using the latest updated values, often leading to faster convergence. Both methods are useful for sparse matrices where direct methods are computationally expensive. At the same time we will also work with sparse datatypes for the first time.

#### Conjugate Gradient (with-/out PreConditioning)
Here, we explore the Conjugate Gradient method, an efficient algorithm for solving large sparse systems of linear equations, particularly those arising from discretizing partial differential equations. The method works by minimizing the quadratic form associated with the linear system. Preconditioning is discussed as a technique to improve convergence rates, where a preconditioner matrix transforms the system into an equivalent one that is easier to solve.

### Directories

Each of the three directories contains:

- programming: Jupyter notebooks with implementations of the discussed algorithms.
- documentation: Detailed reports on the findings and performance analysis for the given tasks.

## Getting Started

### Prerequisites

Ensure you have the following libraries installed:

- NumPy
- SciPy
- Matplotlib

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. 
See the [LICENSE](LICENSE) file for details.


