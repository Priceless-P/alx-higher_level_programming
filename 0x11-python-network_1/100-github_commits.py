#!/usr/bin/python3
"""
10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    header = {
        'Accept': "application/vnd.github+json",
        'Authorization': "Bearer <Token>",
        'X-GitHub-Api-Version': "2022-11-28"
    }

    response = requests.get(url, headers=header)
    commits = response.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
