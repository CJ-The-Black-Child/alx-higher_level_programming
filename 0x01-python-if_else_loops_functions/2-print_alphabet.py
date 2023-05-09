#!/usr/bin/python3
# so to Loop through the ASCII values for lowercase letters
for i in range(97, 123):
    # print the corresponding character, followed by no space or new line
    print("{:c}".format(i), end="")
