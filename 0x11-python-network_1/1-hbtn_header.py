#!/usr/bin/python3
"""
Script that takes in a URL, send a request and displays the value
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request_url = urllib.request.Request(url)
    with urllib.request.urlopen(request_url) as response:
        print(dict(response.headers).get("X-Request-Id"))
