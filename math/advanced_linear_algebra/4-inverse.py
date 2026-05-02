#!/usr/bin/env python3
"""Inverse of a matrix"""


def determinant(matrix):
    """Compute determinant"""

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
    """Compute cofactor matrix"""

    n = len(matrix)

    if n == 1:
        return [[1]]

    cof = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [
                [matrix[x][y] for y in range(n) if y != j]
                for x in range(n) if x != i
            ]
            row.append(((-1) ** (i + j)) * determinant(sub))
        cof.append(row)

    return cof


def adjugate(matrix):
    """Compute adjugate matrix"""

    cof = cofactor(matrix)

    n = len(matrix)
    return [
        [cof[j][i] for j in range(n)]
        for i in range(n)
    ]


def inverse(matrix):
    """Calculates inverse of a matrix"""

    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if matrix == [] or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)

    if det == 0:
        return None

    adj = adjugate(matrix)

    return [
        [adj[i][j] / det for j in range(n)]
        for i in range(n)
    ]
