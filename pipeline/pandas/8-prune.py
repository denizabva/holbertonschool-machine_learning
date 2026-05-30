#!/usr/bin/env python3
"""
This module contains a function that removes NaN values from a DataFrame.
"""


def prune(df):
    """
    Removes any rows where Close column has NaN values.

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        pd.DataFrame: cleaned dataframe
    """
    return df.dropna(subset=["Close"])
