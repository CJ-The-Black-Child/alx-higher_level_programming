#!/usr/bin/python3
"""
A script that lists 10 commits (from the most recent to
oldest of a specified repo by the user)
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    owner = sys.argv[2]
    repository = sys.argv[1]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    try:
        response = requests.get(url)
        commits = response.json()

        for i in range(10):
            commit = commits[i]
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except IndexError:
        pass
