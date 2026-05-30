#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def bars():
    np.random.seed(1)

    people = ["Farrah", "Fred", "Felicia"]
    apples = np.array([18, 15, 20])
    bananas = np.array([22, 30, 25])
    oranges = np.array([25, 20, 15])
    peaches = np.array([10, 5, 12])

    x = np.arange(len(people))

    plt.bar(x, apples, width=0.5, color="red", label="apples")
    plt.bar(x, bananas, bottom=apples, width=0.5,
            color="yellow", label="bananas")
    plt.bar(x, oranges, bottom=apples + bananas, width=0.5,
            color="#ff8000", label="oranges")
    plt.bar(x, peaches, bottom=apples + bananas + oranges,
            width=0.5, color="#ffe5b4", label="peaches")

    plt.ylabel("Quantity of Fruit")
    plt.title("Number of Fruit per Person")

    plt.xticks(x, people)
    plt.yticks(range(0, 81, 10))
    plt.ylim(0, 80)

    plt.legend()

    plt.show()
