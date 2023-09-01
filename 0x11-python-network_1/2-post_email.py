#!/usr/bin/python3
"""
This script will take a URL and an email as argument, sends a POST request
to the URL with the email as a parameter, and displays the body of
the response
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    """ Create a dictionary with the email parameter """
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    """ Create a request object and send the POST request """
    request = urllib.request.Request(url, data)

    """ Obtain the response and decode it """
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
