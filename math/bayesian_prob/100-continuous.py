#!/usr/bin/env python3
"""Calculates posterior probability over a continuous range"""

from scipy import special


def posterior(x, n, p1, p2):
    """Calculates probability that p is in [p1, p2] given x and n"""

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

    # Check p1
    if not isinstance(p1, float) or p1 < 0 or p1 > 1:
        raise ValueError(
            "p1 must be a float in the range [0, 1]"
        )

    # Check p2
    if not isinstance(p2, float) or p2 < 0 or p2 > 1:
        raise ValueError(
            "p2 must be a float in the range [0, 1]"
        )

    # Check p2 > p1
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    # Posterior parameters (Beta distribution)
    a = x + 1
    b = n - x + 1

    # Compute probability using CDF difference
    prob = special.betainc(a, b, p2) - special.betainc(a, b, p1)

    return prob
