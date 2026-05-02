#!/usr/bin/env python3
"""Determinant of a matrix"""


def determinant(matrix):
    """Calculates determinant of a square matrix"""

    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1

    if matrix == []:
        raise ValueError("matrix must be a square matrix")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    det = 0
    for col in range(n):
        sub_matrix = []

        for i in range(1, n):
            sub_matrix.append(
                [matrix[i][j] for j in range(n) if j != col]
            )

        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(sub_matrix)

    return det
