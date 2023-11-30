#!/usr/bin/python3
"""
    Module with function that prints a square
"""


def print_square(size):
    """
    Prints a square with # character

    :param size: int

    :return: None

    :raises: TypeError: when first_name or last_name is not a string
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
