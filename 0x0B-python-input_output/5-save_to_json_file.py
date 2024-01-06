#!/usr/bin/python3

""" module for learning saving to json files"""

import json


def save_to_json_file(my_obj, filename):
    """saves json representation of object to file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
