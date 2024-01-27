#!/usr/bin/python3

"""
Python script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import sys
import requests

if __name__ == "__main__":

    URL = sys.argv[1]
    req = requests.get(URL)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
