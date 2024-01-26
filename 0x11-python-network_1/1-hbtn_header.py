#!/usr/bin/python3

"""
Python script that takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id
variable found in the header of the response.
"""

import sys
import urllib.request

URL = sys.argv[1]

req = urllib.request.Request(URL)
with urllib.request.urlopen(URL) as response:
    print(dict(response.headers).get("X-Request-Id"))
