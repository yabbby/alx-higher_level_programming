#!/usr/bin/python3

"""
    module to learn inheritance in python
"""


def is_kind_of_class(obj, a_class):
    """checks if obj is instance of a_class or other subclasses of a_class"""
    return isinstance(obj, a_class)
