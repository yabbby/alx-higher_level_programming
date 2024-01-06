#!/usr/bin/python3

""" Module with square class"""

import json

from .rectangle import Rectangle


class Square(Rectangle):
    """class representing a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for size"""
        self.validate_input("width", size)
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updates properties of the square instance"""
        if args and len(args) != 0:
            keys = list(self.__dict__)
            for i, arg in enumerate(args):
                setattr(self, keys[i], arg)
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns a dictionary representation of square instance"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """returns a string representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
