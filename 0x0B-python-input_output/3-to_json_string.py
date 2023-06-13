#!/usr/bin/python3
"""
imports the Json dictionary
"""
import json
""" define a function to_json_string"""


def to_json_string(my_obj):
    """
    Function to return the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
