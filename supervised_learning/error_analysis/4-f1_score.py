#!/usr/bin/env python3
"""Calculates the F1 score for each class."""

import numpy as np

sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    Calculates the F1 score for each class.

    Args:
        confusion (numpy.ndarray): Confusion matrix of shape
                                   (classes, classes)

    Returns:
        numpy.ndarray: F1 score for each class.
    """
    recall = sensitivity(confusion)
    prec = precision(confusion)

    return 2 * (prec * recall) / (prec + recall)
