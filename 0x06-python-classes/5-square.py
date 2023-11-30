#!/usr/bin/python3
"""square class main"""


class Square:
    """square class"""
    __size = None

    def __init__(self, size=0):
        """Constructor of class Square
        Arguments:
            @size: size of side of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """getter of size
        Return:
            value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of the size
        Arguments:
            value: value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return:
            area of square"""
        return self.__size * self.__size

    def my_print(self):
        """ square made using the character #
            or a blank line if @size == 0"""
        if self.size == 0:
            print()
            return
        for i in range(1, self.size + 1):
            print("#" * self.size)
