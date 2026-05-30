#!/usr/bin/env python3
"""
This module contains a function that cleans and fills missing DataFrame values.
"""


def fill(df):
    """
    Cleans dataframe by removing and filling missing values.

    Rules:
    - Remove Weighted_Price column
    - Fill Close NaNs with previous value
    - Fill Open, High, Low NaNs with Close
    - Fill Volume columns with 0

    Args:
        df (pd.DataFrame): input dataframe

    Returns:
        pd.DataFrame: cleaned dataframe
    """
    df = df.drop(columns=["Weighted_Price"])

    df["Close"] = df["Close"].fillna(method="ffill")

    df["Open"] = df["Open"].fillna(df["Close"])
    df["High"] = df["High"].fillna(df["Close"])
    df["Low"] = df["Low"].fillna(df["Close"])

    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

    return df
