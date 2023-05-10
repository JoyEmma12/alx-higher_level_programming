#!/usr/bin/python3
"""Script that fetches url"""

import urllib.request


if __name__ == "__main__":
	request_url = urllib.request.Request("https://alx-intranet.hbtn.io/status")
	with urllib.request.urlopen(request_url) as response:
		the_page = response.read()
		print("Body response:")
		print("\t- type: {}".format(type(the_page)))
		print("\t- content: {}".format(the_page))
		print("\t- utf8 content: {}".format(the_page.decode("utf-8")))
