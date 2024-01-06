#!/usr/bin/python3

""" module to learn how to convert classes to json representation"""


class Student:
    """class representing a student"""

    def __init__(self, first_name, last_name, age):
        """constructor of student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns json representation of student"""
        if attrs is not None:
            final_dict = {}
            for attr in self.__dict__:
                if attr in attrs:
                    final_dict[attr] = self.__dict__[attr]

            return final_dict

        return self.__dict__

    def reload_from_json(self, json):
        for attribute in json:
            if hasattr(self, attribute):
                setattr(self, attribute, json[attribute])
