#!/usr/bin/python3
"""
A Script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    rq = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(rq.text).__name__}")
    print(f"\t- content: {rq.text}")
