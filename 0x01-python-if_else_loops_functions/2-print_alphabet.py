#!/usr/bin/python3

# print the first characters int the range
print("{:c}".format(97), end="")

# so to Loop through the ASCII values for lowercase letters
for i in range(98, 123):
    # print the corresponding character, followed by no space or new line
    print("{:c}".format(i), end="")
