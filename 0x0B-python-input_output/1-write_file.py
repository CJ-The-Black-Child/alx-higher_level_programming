#!/usr/bin/python3
""" Define a function write_file """


def write_file(filename="", text=""):
    """
    Function to write a string to a text file (UTF8) and return
    the number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
