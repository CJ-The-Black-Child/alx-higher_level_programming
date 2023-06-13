#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Function to append a string at the end of a text file (UTF8) and return
    the number of characters added.

    Args:
        filename (str): The name of the file to which the string
                        will be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return num_characters_added
