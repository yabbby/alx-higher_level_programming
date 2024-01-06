#!/usr/bin/python3

""" Module with rectangle model """

from .base import Base


class Rectangle(Base):
    """Class representing a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for rectangle class"""
        super().__init__(id)
        self.validate_input("width", width)
        self.validate_input("height", height)
        self.validate_input("x", x)
        self.validate_input("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validate_input(self, name, value):
        """validates the given input"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width"""
        self.validate_input("width", width)
        self.__width = width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""
        self.validate_input("height", height)
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        self.validate_input("x", x)
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        self.validate_input("y", y)
        self.__y = y

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle instance with # character representing it"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """updates the rectangle class"""
        if args and args != []:
            keys = list(self.__dict__)
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns a dictionary representation of the rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }

    def __str__(self):
        """returns the string representation of the rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} "
            f"- {self.width}/{self.height}"
        )
