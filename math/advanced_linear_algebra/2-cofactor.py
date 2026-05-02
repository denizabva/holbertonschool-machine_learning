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
        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(sub)

    return det


def minor(matrix):
    """Compute minor matrix"""

    n = len(matrix)
    return [
        [
            determinant([
                [matrix[i][j] for j in range(n) if j != col]
                for i in range(n) if i != row
            ])
            for col in range(n)
        ]
        for row in range(n)
    ]


def cofactor(matrix):
    """Calculates the cofactor matrix of a square matrix"""

    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if matrix == [] or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    minor_matrix = minor(matrix)

    return [
        [
            minor_matrix[i][j] * ((-1) ** (i + j))
            for j in range(n)
        ]
        for i in range(n)
    ]
