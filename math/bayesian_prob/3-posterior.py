#!/usr/bin/env python3
"""Calculates the posterior probability"""

import numpy as np


def posterior(x, n, P, Pr):
    """Calculates the posterior probability"""

    # Check n
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Check x
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )

    # Check x <= n
    if x > n:
        raise ValueError("x cannot be greater than n")

    # Check P
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    # Check Pr
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P"
        )

    # Check values in P
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError(
            "All values in P must be in the range [0, 1]"
        )

    # Check values in Pr
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError(
            "All values in Pr must be in the range [0, 1]"
        )

    # Check sum of Pr
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Likelihood (binomial without coefficient)
    likelihood = (P ** x) * ((1 - P) ** (n - x))

    # Unnormalized posterior
    posterior_unnormalized = likelihood * Pr

    # Normalize
    posterior = posterior_unnormalized / np.sum(
        posterior_unnormalized
    )

    return posterior
