#!/usr/bin/env python3
"""Creates a confusion matrix."""

import numpy as np


def create_confusion_matrix(labels, logits):
    """
    Creates a confusion matrix.

    Args:
        labels (numpy.ndarray): One-hot array of correct labels
                                of shape (m, classes)
        logits (numpy.ndarray): One-hot array of predicted labels
                                of shape (m, classes)

    Returns:
        numpy.ndarray: Confusion matrix of shape (classes, classes)
    """
    classes = labels.shape[1]
    confusion = np.zeros((classes, classes))

    true_labels = np.argmax(labels, axis=1)
    pred_labels = np.argmax(logits, axis=1)

    for true, pred in zip(true_labels, pred_labels):
        confusion[true][pred] += 1

    return confusion
