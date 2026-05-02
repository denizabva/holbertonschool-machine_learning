#!/usr/bin/env python3
"""
Function that calculates the shape of a matrix.
"""


def matrix_shape(matrix):
    """
    Returns the shape of a matrix as a list of integers.

    Args:
        matrix (list): a nested list representing a matrix

    Returns:
        list: shape of the matrix
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
