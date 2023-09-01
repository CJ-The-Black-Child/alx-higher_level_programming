#!/usr/bin/python3
"""
This script takes a URL as an argument
Sends a request to the URL and then displays the body of the response
(decoded in utf-8).
It then handles urllib.error.HTTPError exception
and prints the HTTP status code in case of an error.
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
