#!/usr/bin/env python3
"""
This module concatenates two DataFrames using a hierarchical index.
"""

import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Creates a hierarchical DataFrame with Timestamp as first index level.

    Args:
        df1 (pd.DataFrame): coinbase dataframe
        df2 (pd.DataFrame): bitstamp dataframe

    Returns:
        pd.DataFrame: concatenated hierarchical dataframe
    """
    df1 = index(df1)
    df2 = index(df2)

    df1 = df1.loc[(df1.index >= 1417411980) & (df1.index <= 1417417980)]
    df2 = df2.loc[(df2.index >= 1417411980) & (df2.index <= 1417417980)]

    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])

    # swap index levels so Timestamp becomes first level
    df = df.swaplevel(0, 1).sort_index()

    return df
