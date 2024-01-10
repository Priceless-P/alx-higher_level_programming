#!/usr/bin/python3
"""
Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        response_json = response.json()
        if response_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(response_json.get('id'),
                                   response_json.get('name')))
    except ValueError:
        print("Not a valid JSON")
