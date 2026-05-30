#!/usr/bin/env python3
"""
This module contains a function that extracts data from a DataFrame
and converts it into a numpy array.
"""


def array(df):
    """
    Selects the last 10 rows of High and Close columns
    and converts them into a numpy array.

    Args:
        df (pd.DataFrame): input dataframe with High and Close columns

    Returns:
        numpy.ndarray: extracted values as array
    """
    return df[["High", "Close"]].tail(10).to_numpy()
