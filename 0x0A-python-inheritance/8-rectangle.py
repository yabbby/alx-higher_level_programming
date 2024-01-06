#!/usr/bin/python3

""" module with Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class representing a rectangle"""

    def __init__(self, width, height):
        """constructor for rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
