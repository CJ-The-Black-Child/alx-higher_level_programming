#!/usr/bin/python3
"""
A script that takes a letter as an argument,
sends a POST request to http://0.0.0.0:5000/search_user
with the letters as a parameter,
and displays the result.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    payload = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_response = response.json()
        if json_response:
            print(
                    "[{}] {}".format(
                        json_response.get("id"), json_response.get("name")
                        )
                    )
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
