#!/usr/bin/env python3
import pandas as pd
import string

def from_numpy(array):
    """
    Creates a pandas DataFrame from a numpy ndarray.
    Columns are labeled A, B, C... in alphabetical order.
    """
    cols = list(string.ascii_uppercase[:array.shape[1]])
    return pd.DataFrame(array, columns=cols)
