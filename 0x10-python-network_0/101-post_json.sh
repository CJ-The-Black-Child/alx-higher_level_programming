#!/bin/bash
# Send JSON POST request to URL with file contents and displays response body
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
