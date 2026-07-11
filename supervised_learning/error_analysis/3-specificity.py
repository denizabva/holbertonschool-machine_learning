#!/usr/bin/env python3
"""Calculates the specificity for each class."""

import numpy as np


def specificity(confusion):
    """
    Calculates the specificity for each class.

    Args:
        confusion (numpy.ndarray): Confusion matrix of shape
                                   (classes, classes)

    Returns:
        numpy.ndarray: Specificity of each class.
    """
    true_positives = np.diag(confusion)
    false_positives = np.sum(confusion, axis=0) - true_positives
    false_negatives = np.sum(confusion, axis=1) - true_positives

    total = np.sum(confusion)
    true_negatives = (
        total - (true_positives + false_positives + false_negatives)
    )

    return true_negatives / (true_negatives + false_positives)
