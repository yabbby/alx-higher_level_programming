#!/usr/bin/python3
"""Fetch alx-intranet using urllib"""
from urllib import request

if __name__ == "__main__":
    req = request.Request("https://alx-intranet.hbtn.io/status")
    with request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print(f"\t- type: {type(the_page)}")
        print(f"\t- content: {the_page}")
        html = the_page.decode("UTF-8")
        print(f"\t- utf8 content: {html}")
