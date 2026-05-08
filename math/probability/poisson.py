#!/usr/bin/env python3
"""Poisson distribution class"""


class Poisson:
    """Represents a Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Initialize Poisson distribution"""
        self.lambtha = float(lambtha)

        if data is None:
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates PMF for k successes"""
        if k < 0:
            return 0

        k = int(k)

        e = 2.7182818285 ** (-self.lambtha)

        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        return (self.lambtha ** k) * e / factorial
