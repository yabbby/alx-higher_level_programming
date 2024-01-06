#!/usr/bin/python3

""" module to learn how to convert classes to json representation"""


class Student:
    """class representing a student"""

    def __init__(self, first_name, last_name, age):
        """constructor of student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns json representation of student"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
        }
