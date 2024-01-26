#!/usr/bin/python3
"""
python code to fetch a website using
urllib module from python
"""

import urllib.request


if __name__ == "__main__":
    send_req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(send_req) as f:
        html = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
