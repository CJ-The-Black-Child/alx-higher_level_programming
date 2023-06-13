#!/usr/bin/python3
"""
A script to add items to a JSON file
"""
import sys
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

# Load existing items from file
try:
    items = load_from_json_file('add_item.json')
except FileNotFoundError:
    items = []

# Add new items from command line Arguments
items.extend(sys.argv[1:])

# Save Updated items to file
save_to_json_file(items, 'add_item.json')
