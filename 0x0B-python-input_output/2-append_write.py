#!/usr/bin/python3

""" module for learning how to handle text files in python"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
