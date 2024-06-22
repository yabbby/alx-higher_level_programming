#!/usr/bin/python3
"""Make a post request using requests module"""

from sys import argv

import requests

if __name__ == "__main__":
    URL = argv[1]
    EMAIL = argv[2]
    r = requests.post(URL, data={"email": EMAIL})
    print(r.text)
