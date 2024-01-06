#!/usr/bin/python3

""" Base class module"""

import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns a python object deserialized from json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a json string representation of list_objs to a file"""
        final_list = []
        with open(f"{cls.__name__}.json", "w") as f:
            for obj in list_objs:
                final_list.append(obj.to_dictionary())
            f.write(cls.to_json_string(final_list))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances from file"""
        f_name = "{}.json".format(cls.__name__)
        try:
            with open(f_name, mode="r", encoding="utf-8") as file:
                f_output = file.read().replace("'", '"')
            dicts = cls.from_json_string(f_output)
            instances = []
            for dict in dicts:
                instances.append(cls.create(**dict))
            return instances
        except IOError:
            return []
