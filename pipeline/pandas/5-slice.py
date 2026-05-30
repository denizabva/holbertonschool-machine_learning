#!/usr/bin/env python3
"""
This module contains a function that slices a DataFrame.
"""


def slice(df):
    """
    Extracts High, Low, Close, and Volume_(BTC) columns
    and selects every 60th row.

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        pd.DataFrame: sliced dataframe
    """
    return df[["High", "Low", "Close", "Volume_(BTC)"]][::60]
