#!/usr/bin/python3
"""
 Python script that takes your GitHub credentials
 (username and password) and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    header = {
        'Accept': "application/vnd.github+json",
        'X-GitHub-Api-Version': "2022-11-28"}
    auth = HTTPBasicAuth(username, password)

    response = requests.get(url, headers=header, auth=auth)
    print(response.json().get('id'))
