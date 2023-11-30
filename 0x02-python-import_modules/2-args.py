#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    if length == 1:
        print("{} argument:".format(length))
    elif length == 0:
        print("{} arguments.".format(length))
    else:
        print("{} arguments:".format(length))

    if length >= 1:
        for i, arg in enumerate(argv[1:]):
            print("{}: {}".format(i + 1, arg))
