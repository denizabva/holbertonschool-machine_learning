#!/usr/bin/env python3
"""Minor of a matrix"""


def determinant(matrix):
    """Helper function to compute determinant"""

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    det = 0
    for col in range(n):
        sub = []
        for i in range(1, n):
            sub.append([matrix[i][j] for j in range(n) if j != col])

        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(sub)

    return det


def minor(matrix):
    """Calculates the minor matrix of a square matrix"""

    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if matrix == [] or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # 1x1 matrix
    if n == 1:
        return [[1]]

    minor_matrix = []

    for i in range(n):
        row_minors = []
        for j in range(n):
            sub_matrix = [
                [matrix[x][y] for y in range(n) if y != j]
                for x in range(n) if x != i
            ]
            row_minors.append(determinant(sub_matrix))
        minor_matrix.append(row_minors)

    return minor_matrix
