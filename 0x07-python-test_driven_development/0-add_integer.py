#!/usr/bin/python3
"""
    Addition module
"""


def add_integer(a, b=98):
    """
    Calculates the sum of two numbers

    :param a: int | float
    :param b: int | float

    :return: float | int, the sum of the two numbers

    :raises: TypeError, when a or b is not an int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
