#!/usr/bin/env python3
"""Determinant of a matrix"""


def determinant(matrix):
    """Calculates determinant of a square matrix"""

    # Validate type: must be list of lists
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Empty matrix case: [[]] represents 0x0 matrix
    if matrix == [[]]:
        return 1

    # Matrix must not be empty
    if matrix == [] or len(matrix) == 0:
        raise ValueError("matrix must be a square matrix")

    n = len(matrix)

    # Must be square
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    # Recursive case (Laplace expansion)
    det = 0
    for col in range(n):
        sub_matrix = []

        for i in range(1, n):
            row = []
            for j in range(n):
                if j != col:
                    row.append(matrix[i][j])
            sub_matrix.append(row)

        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(sub_matrix)

    return det
