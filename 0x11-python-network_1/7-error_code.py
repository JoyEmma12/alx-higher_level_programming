#!/usr/bin/python3
"""
Script that checks if the HTTP status code
Is greater than or equal to 400
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
