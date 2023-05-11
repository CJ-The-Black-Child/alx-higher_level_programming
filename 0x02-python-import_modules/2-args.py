#!/usr/bin/env python3
from sys import argv

if len(argv) == 1:
    print("0 arguments.")
else:
    n = len(argv) - 1
    if n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))
    for i in range(1, len(argv)):
        print("{}:{}".format(i, argv[i]))
