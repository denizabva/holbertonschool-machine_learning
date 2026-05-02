#!/usr/bin/env python3
"""
Function that adds two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of lists): first matrix
        mat2 (list of lists): second matrix

    Returns:
        list of lists or None: new matrix or None if shapes differ
    """
    if len(mat1) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None

        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])

        result.append(row)

    return result
