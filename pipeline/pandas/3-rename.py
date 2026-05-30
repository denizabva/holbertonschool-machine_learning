#!/usr/bin/env python3
"""
This module renames and formats a DataFrame column.
"""

import pandas as pd


def rename(df):
    """
    Converts Timestamp to Datetime and returns only Datetime and Close columns.

    Args:
        df (pd.DataFrame): input dataframe containing Timestamp column

    Returns:
        pd.DataFrame: modified dataframe
    """
    df = df.copy()

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s")
    df = df.rename(columns={"Timestamp": "Datetime"})

    return df[["Datetime", "Close"]]
