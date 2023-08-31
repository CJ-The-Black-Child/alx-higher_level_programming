#!/bin/bash
# Send a DELETE request to the URL and display the response body
curl -sfL "$1" -X DELETE
