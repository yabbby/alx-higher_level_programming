#!/usr/bin/python3
"""Make a post request using requests module"""
from sys import argv
import requests

if __name__ == "__main__":
    URL = argv[1]
    r = requests.get(URL)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
