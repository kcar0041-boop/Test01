import numpy as np

def multiply_matrices(matrix_a, matrix_b):
    """Multiplies two 3x3 matrices.

    Args:
        matrix_a (list of lists): The first 3x3 matrix.
        matrix_b (list of lists): The second 3x3 matrix.

    Returns:
        list of lists: The product of the two matrices.

    Raises:
        ValueError: If either input matrix is not 3x3.
    """
    # Validate that both input matrices are 3x3
    if len(matrix_a) != 3 or len(matrix_a[0]) != 3 or \
       len(matrix_b) != 3 or len(matrix_b[0]) != 3:
        raise ValueError("Both matrices must be 3x3")

    # Initialize a 3x3 result matrix with zeros
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    # Perform matrix multiplication using three nested loops
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def determinant_3x3(matrix):
    """Calculates the determinant of a 3x3 matrix.

    Args:
        matrix (list of lists): The 3x3 matrix to calculate the determinant for.

    Returns:
        int or float: The determinant of the matrix.

    Raises:
        ValueError: If the input matrix is not 3x3.
    """
    # Validate that the input matrix is 3x3
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError("Matrix must be 3x3 to calculate determinant")

    # Extract elements of the first row for calculation
    a, b, c = matrix[0]
    # Extract elements of the second row
    d, e, f = matrix[1]
    # Extract elements of the third row
    g, h, i = matrix[2]

    # Calculate the determinant using the Sarrus' rule formula for a 3x3 matrix
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det

def multiply_and_determinant_3x3(matrix_a, matrix_b):
    """Multiplies two 3x3 matrices and returns the product and its determinant.

    This function orchestrates the multiplication of two matrices
    and then calculates the determinant of their product.

    Args:
        matrix_a (list of lists): The first 3x3 matrix.
        matrix_b (list of lists): The second 3x3 matrix.

    Returns:
        tuple: A tuple containing:
            - list of lists: The product matrix.
            - int or float: The determinant of the product matrix.
    """
    # Call the separate function to multiply the two matrices
    product_matrix = multiply_matrices(matrix_a, matrix_b)
    # Call the separate function to calculate the determinant of the product matrix
    det_product = determinant_3x3(product_matrix)
    return product_matrix, det_product

print("Created matrix_operations.py")
