#!/usr/bin/python3

"""
    module with function checking if a object is an exact instance of a class
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is an exact instance of a_class
    """
    return type(obj) == a_class
