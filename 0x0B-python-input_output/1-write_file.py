#!/usr/bin/python3

""" module for learning how to handle text files in python"""


def write_file(filename="", text=""):
    """writes text to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
