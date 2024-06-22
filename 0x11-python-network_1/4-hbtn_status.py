#!/usr/bin/python3
"""Make a get request using requests module"""
import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    body = r.text
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
