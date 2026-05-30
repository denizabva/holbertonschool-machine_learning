#!/usr/bin/env python3
"""Calculates a correlation matrix"""

import numpy as np


def correlation(C):
    """Calculates the correlation matrix from a covariance matrix"""

    # Check type
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # Check shape (square matrix)
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Diagonal (variances)
    diag = np.diag(C)

    # Standard deviations
    stddev = np.sqrt(diag)

    # Outer product of stddevs
    denom = np.outer(stddev, stddev)

    # Correlation matrix
    R = C / denom

    return R
