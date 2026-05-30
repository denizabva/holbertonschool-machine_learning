#!/usr/bin/env python3
"""Binomial distribution module."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize a Binomial distribution."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - (variance / mean)
            self.n = round(mean / p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Calculates the PMF for a given number of successes."""
        if k < 0:
            return 0

        k = int(k)
        if k > self.n:
            return 0

        factorial_n = 1
        factorial_k = 1
        factorial_n_k = 1

        for i in range(1, self.n + 1):
            factorial_n *= i
        for i in range(1, k + 1):
            factorial_k *= i
        for i in range(1, self.n - k + 1):
            factorial_n_k *= i

        combination = factorial_n / (factorial_k * factorial_n_k)

        return combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates the CDF for a given number of successes."""
        if k < 0:
            return 0

        k = int(k)
        if k > self.n:
            return 0

        result = 0
        for i in range(k + 1):
            result += self.pmf(i)

        return result
