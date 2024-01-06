#!/usr/bin/python3
"""module square"""


class Square:
    """square class"""
    __size = None

    def __init__(self, size=0):
        """constructor of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
