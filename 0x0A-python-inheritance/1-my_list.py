#!/usr/bin/python3
"""This contains a MyList class"""


class MyList(list):
    """Custom list class that inhertis from the buit-in list class."""

    def print_sorted(self):
        """Prints the list elements in sorted (ascending) order. """
        sorted_list = sorted(self)
        print(sorted_list)
