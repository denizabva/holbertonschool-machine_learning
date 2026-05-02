#!/usr/bin/env python3
"""
Function that performs element-wise operations on numpy arrays.
"""


def np_elementwise(mat1, mat2):
    """
    Returns element-wise sum, difference, product, and quotient.

    Args:
        mat1 (numpy.ndarray): first input array
        mat2 (numpy.ndarray or scalar): second input

    Returns:
        tuple: (sum, difference, product, quotient)
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
