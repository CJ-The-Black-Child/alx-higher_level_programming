#!/usr/bin/python3
"""defines a json_string function"""
import json


def from_json_string(my_str):
    """
    Function to return an object (Python data structure) represented by a JSON
    string.

    Args:
        my_str (str): The JSON string to be converted to an object.

    Returns:
        object: The Python data structure representede by the JSON string.
    """
    return json.loads(my_str)
