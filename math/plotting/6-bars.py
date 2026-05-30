#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
grades = np.random.randint(0, 100, 50)

bins = range(0, 101, 10)

plt.hist(
    grades,
    bins=bins,
    edgecolor='black'
)

plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Project A")

plt.show()
