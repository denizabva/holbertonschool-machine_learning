#!/usr/bin/env python3
"""Calculates the precision for each class."""

import numpy as np


def precision(confusion):
    """
    Calculates the precision for each class.

    Args:
        confusion (numpy.ndarray): Confusion matrix of shape
                                   (classes, classes)

    Returns:
        numpy.ndarray: Precision of each class.
    """
    true_positives = np.diag(confusion)
    false_positives = np.sum(confusion, axis=0) - true_positives

    return true_positives / (true_positives + false_positives)
