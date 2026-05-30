#!/usr/bin/env python3
"""Multivariate Normal distribution class"""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Class constructor"""

        # Validate input type and dimension
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        # Check number of data points
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Compute mean (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center data
        data_centered = data - self.mean

        # Compute covariance (d, d)
        self.cov = np.matmul(data_centered, data_centered.T) / (n - 1)
