#!/usr/bin/env python3
"""
This module concatenates two DataFrames based on Timestamp index.
"""

import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Indexes both dataframes on Timestamp, filters df2,
    and concatenates df2 (bitstamp) above df1 (coinbase).

    Args:
        df1 (pd.DataFrame): coinbase dataframe
        df2 (pd.DataFrame): bitstamp dataframe

    Returns:
        pd.DataFrame: concatenated dataframe with keys
    """
    df1 = index(df1)
    df2 = index(df2)

    df2 = df2.loc[df2.index <= 1417411920]

    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
