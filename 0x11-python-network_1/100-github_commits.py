#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to
list 10 commits from recent to oldest of the
repository rails by the user rails
"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
