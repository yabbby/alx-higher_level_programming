#!/usr/bin/python3

""" module for learning json deserialization"""

import json


def from_json_string(my_str):
    """returns an object from a json string"""
    return json.loads(my_str)
