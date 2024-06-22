#!/usr/bin/python3
"""Takes a url and displays the header of response"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    URL = argv[1]
    with request.urlopen(URL) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
