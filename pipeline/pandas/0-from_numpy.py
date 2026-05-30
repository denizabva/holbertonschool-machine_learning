#!/usr/bin/env python3
import pandas as pd


def from_numpy(array):
    """
    Creates a pandas DataFrame from a numpy ndarray.
    Columns are labeled A, B, C... in alphabetical order.
    """
    cols = [chr(ord('A') + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=cols)
