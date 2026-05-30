#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# 1. Remove Weighted_Price
df = df.drop(columns=["Weighted_Price"])

# 2. Rename Timestamp to Date
df = df.rename(columns={"Timestamp": "Date"})

# 3. Convert to datetime
df["Date"] = pd.to_datetime(df["Date"], unit="s")

# 4. Set index
df = df.set_index("Date")

# 5. Fill missing values
df["Close"] = df["Close"].fillna(method="ffill")

df["Open"] = df["Open"].fillna(df["Close"])
df["High"] = df["High"].fillna(df["Close"])
df["Low"] = df["Low"].fillna(df["Close"])

df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

# 6. Filter from 2017 onwards
df = df.loc[df.index >= "2017-01-01"]

# 7. Resample daily with required aggregation
df = df.resample("D").agg({
    "High": "max",
    "Low": "min",
    "Open": "mean",
    "Close": "mean",
    "Volume_(BTC)": "sum",
    "Volume_(Currency)": "sum"
})

# 8. Plot
df.plot()
plt.show()

# 9. Return dataframe
print(df)
