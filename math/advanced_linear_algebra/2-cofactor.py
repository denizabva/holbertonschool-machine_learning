#!/usr/bin/env python3
"""Cofactor matrix"""


def determinant(matrix):
    """Compute determinant of a square matrix"""

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    det = 0
    for col in range(n):
        sub = [
            [matrix[i][j] for j in range(n) if j != col]
            for i in range(1, n)
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)

    return det


def cofactor(matrix):
    """Calculates cofactor matrix"""

    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if matrix == [] or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # FIX: 1x1 matrix case
    if n == 1:
        return [[1]]

    cof = []

    for i in range(n):
        row_cof = []
        for j in range(n):
            sub = [
                [matrix[x][y] for y in range(n) if y != j]
                for x in range(n) if x != i
            ]
            row_cof.append(((-1) ** (i + j)) * determinant(sub))
        cof.append(row_cof)

    return cof
