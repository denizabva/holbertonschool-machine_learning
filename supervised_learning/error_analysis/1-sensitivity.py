#!/usr/bin/env python3
"""Calculates the sensitivity for each class."""

import numpy as np


def sensitivity(confusion):
    """
    Calculates the sensitivity for each class.

    Args:
        confusion (numpy.ndarray): Confusion matrix of shape
                                   (classes, classes)

    Returns:
        numpy.ndarray: Sensitivity of each class.
    """
    true_positives = np.diag(confusion)
    false_negatives = np.sum(confusion, axis=1) - true_positives

    return true_positives / (true_positives + false_negatives)
