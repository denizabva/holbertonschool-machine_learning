#!/usr/bin/env python3
"""
Function that concatenates two numpy arrays along a specific axis.
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two numpy arrays along a given axis.

    Args:
        mat1 (numpy.ndarray): first matrix
        mat2 (numpy.ndarray): second matrix
        axis (int): axis along which to concatenate

    Returns:
        numpy.ndarray: concatenated array
    """
    return np.concatenate((mat1, mat2), axis=axis)
