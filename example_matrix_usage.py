from matrix_operations import multiply_matrices, determinant_3x3, multiply_and_determinant_3x3

# Example Usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix 1:")
for row in matrix1: print(row)

print("
Matrix 2:")
for row in matrix2: print(row)

# Using the single function defined in a separate cell
product_matrix, det_product = multiply_and_determinant_3x3(matrix1, matrix2)

print("
Product Matrix (Matrix1 * Matrix2) using single function:")
for row in product_matrix: print(row)

print(f"
Determinant of the Product Matrix using single function: {det_product}")

# You can also verify with NumPy for comparison:
# import numpy as np
# print("
Verifying with NumPy:")
# print("NumPy Product Matrix:
", np.dot(matrix1, matrix2))
# print("NumPy Determinant:
", np.linalg.det(np.array(product_matrix)))
