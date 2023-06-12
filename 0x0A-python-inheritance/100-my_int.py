#!/usr/bin/python3
"""Defines a class Myint"""


class MyInt(int):
    """Class representing a rebel integer."""

    def __eq__(self, other):
        """Checks if the integer is not equal to the specified value.

            Args:
                other: The value to compare against.

            Returns:
                True if the integer is not equal to the specified value;
                False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Checks if the integer is equal to the specified value.

            Args:
                other: The value to compare against.

            Returns:
                True if the intger is equal to the specified value;
                False otherwise.
        """
        return super().__eq__(other)
