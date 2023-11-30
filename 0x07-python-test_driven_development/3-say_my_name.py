#!/usr/bin/python3
"""
    Module to say your name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints your name in a prettified manner

    :param first_name: str
    :param last_name: str

    :return: None

    :raises: TypeError: when first_name or last_name is not a string
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
