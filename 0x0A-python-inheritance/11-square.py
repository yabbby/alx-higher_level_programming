#!/usr/bin/python3

""" module with square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class representing a square"""

    def __init__(self, size):
        """constructor for square class"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
