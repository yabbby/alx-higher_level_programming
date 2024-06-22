#!/usr/bin/python3
"""Make a get request using requests module"""
from sys import argv

import requests

if __name__ == "__main__":
    USER = argv[1]
    PASSWD = argv[2]
    try:
        r = requests.get("https://api.github.com/user", auth=(USER, PASSWD))
        body = r.json()
        print(body["id"])
    except Exception:
        print(None)
