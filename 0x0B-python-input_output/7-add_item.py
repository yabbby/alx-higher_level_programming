#!/usr/bin/python3

""" module for learning how to handle json files in python"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
JSON_FILE = "add_item.json"

try:
    obj = load_from_json_file(JSON_FILE)
except FileNotFoundError:
    obj = []
    save_to_json_file(obj, JSON_FILE)

for arg in sys.argv[1:]:
    obj.append(arg)

save_to_json_file(obj, JSON_FILE)
