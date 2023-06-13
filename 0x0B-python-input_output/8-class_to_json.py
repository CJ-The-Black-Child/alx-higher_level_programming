#!/usr/bin/python3
"""
A function to convert a class object to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Convert a class object to a JSON-serializable dictionary.

    Args:
        obj: The object to convert

    Returns:
        dict: A dictionary containing the serializable attributes
        of the object.
    """
    # Get the dictionary of object attributes
    obj_dict = obj.__dict__

    # Check if the object has a '__dict__' attribute (for custom classes)
    if hasattr(obj, '__dict__'):
        obj_dict = obj.__dict__

    # Filter out attribites that are not serializable
    serializable_dict = {
        key:  value
        for key, value in obj_dict.items()
        if isinstance(value, (list, dict, str, int, bool))
    }

    return serializable_dict
