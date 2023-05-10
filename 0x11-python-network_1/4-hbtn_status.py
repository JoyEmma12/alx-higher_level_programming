#!/usr/bin/python3
"""
Script that fetches URL using the request package
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    page = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(page.text)))
    print("\t- content: {}".format(page.text))
