#!/usr/bin/python3
"""defines a function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function to write an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file to which the object will
                        be written.

    Returns:
        None
    """
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
