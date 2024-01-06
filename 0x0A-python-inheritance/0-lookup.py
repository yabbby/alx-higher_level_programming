#!/usr/bin/python3

"""
    module with function that prints all things in namespace.
"""


def lookup(obj):
    """returns the names in the current scope"""
    return dir(obj)
