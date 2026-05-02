#!/usr/bin/env python3
"""
Function that performs matrix multiplication using numpy.
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Multiplies two numpy matrices.

    Args:
        mat1 (numpy.ndarray): first matrix
        mat2 (numpy.ndarray): second matrix

    Returns:
        numpy.ndarray: result of matrix multiplication
    """
    return np.matmul(mat1, mat2)
