#!/usr/bin/python3

""" module for learning how to load objects from json files in python"""

import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
