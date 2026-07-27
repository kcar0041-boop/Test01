import pytest
from matrix_operations import multiply_matrices, determinant_3x3, multiply_and_determinant_3x3

# --- Positive Test Cases ---

def test_multiply_matrices_identity():
    matrix_a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # Identity matrix
    matrix_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert multiply_matrices(matrix_a, matrix_b) == expected

def test_multiply_matrices_zero():
    matrix_a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Zero matrix
    matrix_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert multiply_matrices(matrix_a, matrix_b) == expected

def test_multiply_matrices_standard():
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    expected = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
    assert multiply_matrices(matrix_a, matrix_b) == expected

def test_determinant_3x3_identity():
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected = 1
    assert determinant_3x3(matrix) == expected

def test_determinant_3x3_zero_determinant():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = 0
    assert determinant_3x3(matrix) == expected

def test_determinant_3x3_non_zero():
    matrix = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    expected = -306 # Calculated manually or using a reliable tool
    assert determinant_3x3(matrix) == expected

def test_multiply_and_determinant_3x3_standard():
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    expected_product = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
    expected_determinant = 0
    product, det = multiply_and_determinant_3x3(matrix_a, matrix_b)
    assert product == expected_product
    assert det == expected_determinant

# --- Negative Test Cases ---

def test_multiply_matrices_invalid_dimensions_a():
    matrix_a = [[1, 2], [3, 4]] # 2x2 matrix
    matrix_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError, match="Both matrices must be 3x3"):
        multiply_matrices(matrix_a, matrix_b)

def test_multiply_matrices_invalid_dimensions_b():
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[1, 2], [3, 4]] # 2x2 matrix
    with pytest.raises(ValueError, match="Both matrices must be 3x3"):
        multiply_matrices(matrix_a, matrix_b)

def test_determinant_3x3_invalid_dimensions():
    matrix = [[1, 2], [3, 4]] # 2x2 matrix
    with pytest.raises(ValueError, match="Matrix must be 3x3 to calculate determinant"):
        determinant_3x3(matrix)

def test_multiply_matrices_non_list_input():
    with pytest.raises(TypeError):
        multiply_matrices(123, [[1,0,0],[0,1,0],[0,0,1]])

def test_determinant_3x3_non_list_input():
    with pytest.raises(TypeError):
        determinant_3x3(123)
