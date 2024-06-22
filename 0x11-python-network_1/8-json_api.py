#!/usr/bin/python3
"""Make a post request using requests module"""
from sys import argv

import requests

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        LETTER = argv[1]
    else:
        LETTER = ""

    r = requests.post(URL, data={"q": LETTER})
    try:
        body = r.json()
        if body:
            print(f"[<{body['id']}>] <{body['name']}>")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
