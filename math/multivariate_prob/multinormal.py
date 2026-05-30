#!/usr/bin/env python3
"""Multivariate Normal distribution class"""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Class constructor"""

        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        self.d, self.n = data.shape

        if self.n < 2:
            raise ValueError("data must contain multiple data points")

        # Mean: (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center data
        centered = data - self.mean

        # Covariance: (d, d)
        self.cov = np.matmul(centered, centered.T) / (self.n - 1)

    def pdf(self, x):
        """Calculates the PDF at a data point x"""

        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        if x.shape != (self.d, 1):
            raise ValueError(
                f"x must have the shape ({self.d}, 1)"
            )

        # Mean difference
        diff = x - self.mean

        # Determinant and inverse of covariance
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)

        d = self.d

        # Normalization constant
        norm_const = 1 / (
            ((2 * np.pi) ** (d / 2)) * (det ** 0.5)
        )

        # Exponent term
        exponent = -0.5 * (
            np.matmul(np.matmul(diff.T, inv), diff)
        )

        return float(norm_const * np.exp(exponent)[0][0])
