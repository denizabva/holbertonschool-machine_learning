#!/usr/bin/env python3
"""
This module contains a function that renames and formats a DataFrame column.
"""

import pandas as pd


def rename(df):
    """
    Renames Timestamp column to Datetime, converts it to datetime values,
    and returns only Datetime and Close columns.

    Args:
        df (pd.DataFrame): input dataframe containing Timestamp column

    Returns:
        pd.DataFrame: modified dataframe
    """
    df = df.copy()

    df["Datetime"] = pd.to_datetime(df["Timestamp"], unit="s")
    df = df.rename(columns={"Timestamp": "Datetime"})

    return df[["Datetime", "Close"]]
