#!/usr/bin/python3
"""Define a function that ads attributes to objects."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it is possible.

        Args: The object to add the attribute to.
            name: The name of the attribute.
            value: The value of the attribute.

        Raises:
            TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
