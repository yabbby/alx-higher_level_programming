#!/usr/bin/python3

"""
    module to learn inheritance
"""


class BaseGeometry:
    """Class with functions doing basic geometric operations"""

    def area(self):
        raise Exception("area() is not implemented")
