#!/usr/bin/python3
"""
This script takes a URL and an email address as arguments,
Sends in a POST request to the URL with the email as a parameter,
and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    """ Sends a POST request with the email as a parameter """
    payload = {'email': email}
    response = requests.post(url, data=payload)

    """ Displays the body of the response """
    print(response.text)
