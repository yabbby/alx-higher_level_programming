#!/usr/bin/python3

""" module for learning how to handle text files in python"""


def read_file(filename=""):
    """reads a file with filename"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
