#!/usr/bin/env python3
"""
This module computes descriptive statistics for a DataFrame.
"""


def analyze(df):
    """
    Computes descriptive statistics for all columns except Timestamp.

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        pd.DataFrame: statistics summary
    """
    return df.drop(columns=["Timestamp"]).describe()
