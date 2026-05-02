#!/usr/bin/env python3
"""
Function that adds two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list of int/float): first array
        arr2 (list of int/float): second array

    Returns:
        list or None: new list with summed elements or None if sizes differ
    """
    if len(arr1) != len(arr2):
        return None

    return [arr1[i] + arr2[i] for i in range(len(arr1))]
