#!/usr/bin/env python3
"""Matrix definiteness"""


import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix"""

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.size == 0 or matrix.shape[0] != matrix.shape[1]:
        return None

    # Ensure symmetric matrix (required for definiteness)
    if not np.allclose(matrix, matrix.T):
        return None

    eigs = np.linalg.eigvals(matrix)

    # Numerical tolerance for floating point errors
    eps = 1e-8

    positive = np.all(eigs > eps)
    non_negative = np.all(eigs >= -eps)
    negative = np.all(eigs < -eps)
    non_positive = np.all(eigs <= eps)

    if positive:
        return "Positive definite"

    if non_negative and not positive:
        return "Positive semi-definite"

    if negative:
        return "Negative definite"

    if non_positive and not negative:
        return "Negative semi-definite"

    return "Indefinite"
