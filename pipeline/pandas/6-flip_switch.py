#!/usr/bin/env python3
"""
This module contains a function that flips and switches a DataFrame.
"""


def flip_switch(df):
    """
    Sorts the dataframe in reverse order and transposes it.

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        pd.DataFrame: transformed dataframe
    """
    return df.iloc[::-1].T
