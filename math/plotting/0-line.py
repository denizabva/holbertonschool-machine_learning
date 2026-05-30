#!/usr/bin/env python3
"""Module that plots a cubic line graph"""


import numpy as np
import matplotlib.pyplot as plt


def line():
    """Function that plots y = x^3 as a red line"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    x = np.arange(0, 11)
    plt.plot(x, y, 'r-')
    plt.xlim(0, 10)
