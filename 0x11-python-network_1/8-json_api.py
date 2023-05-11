#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
"""
import requests
import sys

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    letter_q = {"q": q}

    req = requests.post("http://0.0.0.0:5000/search_user", data=letter_q)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
