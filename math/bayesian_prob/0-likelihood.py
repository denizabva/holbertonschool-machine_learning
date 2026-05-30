#!/usr/bin/env python3
"""Calculates likelihoods for binomial data."""

import numpy as np


def factorial(num):
    """Calculate the factorial of num."""
    result = 1
    for value in range(2, num + 1):
        result *= value
    return result


def likelihood(x, n, P):
    """Calculate the likelihood of observing x successes in n trials."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    coefficient = factorial(n) / (factorial(x) * factorial(n - x))
    return coefficient * (P ** x) * ((1 - P) ** (n - x))
