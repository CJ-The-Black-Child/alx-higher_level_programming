#!/bin/bash
#send an OPTIONS request to the URL and then displays the allowed methods
curl -sI "$1" | grep -i Allow | cut -d " " -f2-
