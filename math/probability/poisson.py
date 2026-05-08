#!/usr/bin/env python3
"""Poisson distribution class"""

import math


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
        e = math.exp(-self.lambtha)
        factorial = math.factorial(k)

        return (self.lambtha ** k) * e / factorial

    def cdf(self, k):
        """Calculates the CDF for a given number of successes"""
        if k < 0:
            return 0

        k = int(k)
        result = 0

        for i in range(k + 1):
            result += self.pmf(i)

        return result
