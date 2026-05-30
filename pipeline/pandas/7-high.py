#!/usr/bin/env python3
"""
This module contains a function that sorts a DataFrame by High price.
"""


def high(df):
    """
    Sorts the dataframe by the High column in descending order.

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        pd.DataFrame: sorted dataframe
    """
    return df.sort_values(by="High", ascending=False)
