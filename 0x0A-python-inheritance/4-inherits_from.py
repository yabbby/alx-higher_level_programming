#!/usr/bin/python3

"""
    module to learn inheritance
"""


def inherits_from(obj, a_class):
    """
    checks if obj inherits directly or indirectly from a_class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
