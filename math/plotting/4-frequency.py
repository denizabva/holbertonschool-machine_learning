#!/usr/bin/env python3
"""Module that plots a histogram of student grades"""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Function that plots the distribution of student grades"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    
    # Keep the original figure size from the starter template
    plt.figure(figsize=(6.4, 4.8))
    
    # Plot the histogram with 10-unit bins and black borders
    plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')
    
    # Labels and Titles
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")
    
    # Set explicit X-axis boundaries to match the reference
    plt.xlim(0, 100)

# DO NOT call frequency() or plt.show() here
