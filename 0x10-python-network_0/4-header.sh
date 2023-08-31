#!/bin/bash
# Send GET request to URL with custom header and display the response body
curl -s "$1" -H "X-School-User-Id: 98"
