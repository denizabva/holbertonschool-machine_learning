#!/usr/bin/env python3
"""
This module sets the Timestamp column as the index of a DataFrame.
"""


def index(df):
    """
    Sets Timestamp column as index.

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        pd.DataFrame: dataframe with Timestamp as index
    """
    return df.set_index("Timestamp")
