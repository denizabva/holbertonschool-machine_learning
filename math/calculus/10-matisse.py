#!/usr/bin/env python3
"""
Function that computes derivative of a polynomial
"""


def poly_derivative(poly):
    """
    Returns the derivative of a polynomial represented by a list
    """
    if (not isinstance(poly, list) or len(poly) == 0 or
            not all(isinstance(c, (int, float)) for c in poly)):
        return None

    if len(poly) == 1:
        return [0]

    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])

    if all(c == 0 for c in derivative):
        return [0]

    return derivative
