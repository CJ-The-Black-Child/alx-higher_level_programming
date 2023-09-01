#!/usr/bin/python3
"""
This script does take a URl as argument,
sends a request to the URl,
and then displays the value of the X-Request-Id variable found
in the response header.
"""

import sys
import urllib.request as request

if __name__ == "__main__":
    url = sys.argv[1]

    """ Create a request object """
    req = request.Request(url)

    """ Send the request and obtain the response """
    with request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
