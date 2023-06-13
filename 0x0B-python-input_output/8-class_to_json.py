#!/usr/bin/python3
def class_to_json(obj):
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
