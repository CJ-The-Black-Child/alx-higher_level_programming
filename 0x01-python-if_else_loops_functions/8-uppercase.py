#!/usr/bin/python3
def uppercase(str):

    for c in str:
        char2pr=" "
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
            char2pr=c
        else:
            char2pr=c
        print("{}".format(char2pr), end ="")
    print("")
