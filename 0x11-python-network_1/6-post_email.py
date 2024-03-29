#!/usr/bin/python3
"""
Script that takes in a URL and an email address
Sends a POST request
And displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    req = requests.post(url, data=email)
    print(req.text)
