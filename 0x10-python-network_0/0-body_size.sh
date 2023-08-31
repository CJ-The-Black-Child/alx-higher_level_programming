#!/bin/bash

# Send a request to the UR, display the size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
