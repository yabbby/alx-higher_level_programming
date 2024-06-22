#!/usr/bin/python3
"""Make a post request using urllib"""
from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    URL = argv[1]
    EMAIL = argv[2]
    body_dict = {"email": EMAIL}
    body = parse.urlencode(body_dict).encode("ascii")
    req = request.Request(URL, data=body)
    with request.urlopen(req) as response:
        print(response.read().decode("UTF-8"))
