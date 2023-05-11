#!/usr/bin/env python3
import sys

# Gets all arguments except the script name
args = sys.argv[1:]
total = 0

# Loops through all arguments and then add them to total
for arg in args:
    total += int(arg)
print(total)
