#!/usr/bin/env python3
"""
This module loads data from a file into a pandas DataFrame.
"""

import pandas as pd


def from_file(filename, delimiter):
    """
    Loads data from a file into a pandas DataFrame.

    Args:
        filename (str): file to load from
        delimiter (str): column separator

    Returns:
        pd.DataFrame: loaded dataframe
    """
    return pd.read_csv(filename, delimiter=delimiter)
