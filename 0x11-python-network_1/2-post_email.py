#!/usr/bin/python3
"""
Script that takes URL and an email,
Sends a POST request to the passed URL and
Displays the body of the response in utf-8
"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode("utf-8")
    request_url = urllib.request.Request(url, data)
    with urllib.request.urlopen(request_url) as response:
        print(response.read().decode("utf-8"))
