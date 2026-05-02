#!/usr/bin/env python3
"""
Function that concatenates two 2D matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a given axis.

    Args:
        mat1 (list of lists): first matrix
        mat2 (list of lists): second matrix
        axis (int): axis along which to concatenate (0 or 1)

    Returns:
        list of lists or None: concatenated matrix or None if impossible
    """

    # Axis 0: add rows
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    # Axis 1: add columns
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None

        result = []
        for i in range(len(mat1)):
            result.append(mat1[i][:] + mat2[i][:])
        return result

    return None
