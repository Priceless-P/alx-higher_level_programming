#!/usr/bin/python3
"""
Python script that sends a request to URL and displays the value
of the X-Request-Id variable found in the header
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    header = requests.get(url).headers

    print(header['X-Request-Id'])
