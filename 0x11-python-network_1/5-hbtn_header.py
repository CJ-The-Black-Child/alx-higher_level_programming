#!/usr/bin/python3
"""
This script takes a URl as an argument,
sends a request to the URL, and displays
the value of the variable X-Request-Id
in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    rq = requests.get(url)
    print(rq.headers.get("X-Request-Id"))
