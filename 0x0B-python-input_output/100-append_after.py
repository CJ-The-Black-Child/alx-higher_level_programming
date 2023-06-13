#!/usr/bin/python3
"""
Appends a line of text to a file after each line containing a specified string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a line of text to a file after each line containing a
    specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The specific string to search for
                             in each line of the file.
        new_string (str): The line of text to append after each
                          line containing the search string.
    Note:
            This function modifies the file directly and does not
                          return any value.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
