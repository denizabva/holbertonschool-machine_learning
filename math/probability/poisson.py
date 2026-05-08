#!/usr/bin/env python3
"""Poisson distribution class"""


class Poisson:
    """Represents a Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Initialize the Poisson distribution"""
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
        """Calculates the PMF for a given number of successes"""
        if k < 0:
            return 0

        k = int(k)

        # compute e^-lambda without math module
        e_neg_lambda = 2.7182818285 ** (-self.lambtha)

        # factorial without math module
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        return (self.lambtha ** k) * e_neg_lambda / factorial

    def cdf(self, k):
        """Calculates the CDF for a given number of successes"""
        if k < 0:
            return 0

        k = int(k)
        result = 0

        for i in range(k + 1):
            result += self.pmf(i)

        return result
