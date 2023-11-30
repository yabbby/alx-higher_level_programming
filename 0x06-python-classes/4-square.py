#!/usr/bin/python3
"""square class module"""


class Square:
    """class Square """

    def __init__(self, size=0):
        """Constructor
        Arguments:
            @size: size of square
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return:
            area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
