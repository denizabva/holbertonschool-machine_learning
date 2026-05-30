#!/usr/bin/env python3
"""Calculates intersections for binomial data and priors."""

import numpy as np


def factorial(num):
    """Calculate the factorial of num."""
    result = 1
    for value in range(2, num + 1):
        result *= value
    return result


def intersection(x, n, P, Pr):
    """Calculate the intersection of observing data and priors."""
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
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    coefficient = factorial(n) / (factorial(x) * factorial(n - x))
    likelihood = coefficient * (P ** x) * ((1 - P) ** (n - x))
    return likelihood * Pr
