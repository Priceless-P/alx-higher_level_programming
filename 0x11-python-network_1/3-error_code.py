#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""


if __name__ == '__main__':
    import sys
    from urllib import request, error

    url = sys.argv[1]
    req = request.Request(url)

    try:
        with request.urlopen(req) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
