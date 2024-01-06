#!/usr/bin/python3

""" module to learn how to convert classes to json representation"""


def class_to_json(obj):
    """returns the dictionary representation of a class"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()

    return {}
