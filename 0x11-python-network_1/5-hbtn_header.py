#!/usr/bin/python3
"""Make a get request using requests module"""
from sys import argv

import requests

if __name__ == "__main__":
    URL = argv[1]
    r = requests.get(URL)
    print(r.headers.get("X-Request-Id"))
