#!/usr/bin/python3
def read_file(filename=""):
    """
    Function to read a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        print(content)
