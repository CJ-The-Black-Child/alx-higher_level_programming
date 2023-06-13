#!/usr/bin/python3
"""
A script to add items to a JSON file
"""
import sys
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file.

    Args:
        filename(str): The name of the JSON file to laod.

    Returns:
        The data loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def save_to_json_file(data, filename):
    """
    Save data to a JSON file.

    Args:
        data: The data to be saved.
        filename (str): The name of the JSON file to save.

    """
    with open(filename, 'w') as file:
        json.dump(data, file)


"""
Load existing items from file
"""
try:
    items = load_from_json_file('add_item.json')
except FileNotFoundError:
    items = []

"""
Add new items from command line arguments
"""
items.extend(sys.argv[1:])

"""
Save updated items to file
"""
save_to_json_file(items, 'add_item.json')
