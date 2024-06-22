#!/usr/bin/python3
"""Make a get request using urllib"""
from sys import argv
from urllib import request
from urllib.error import HTTPError

if __name__ == "__main__":
    URL = argv[1]
    try:
        with request.urlopen(URL) as response:
            print(response.read().decode("UTF-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
