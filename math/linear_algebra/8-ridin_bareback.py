#!/usr/bin/env python3
"""
Function that performs matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two 2D matrices.

    Args:
        mat1 (list of lists): first matrix
        mat2 (list of lists): second matrix

    Returns:
        list of lists or None: result matrix or None if not compatible
    """

    # Check if multiplication is possible
    if len(mat1[0]) != len(mat2):
        return None

    result = []

    # Loop over rows of mat1
    for i in range(len(mat1)):
        row = []

        # Loop over columns of mat2
        for j in range(len(mat2[0])):
            total = 0

            # Dot product
            for k in range(len(mat2)):
                total += mat1[i][k] * mat2[k][j]

            row.append(total)

        result.append(row)

    return result
