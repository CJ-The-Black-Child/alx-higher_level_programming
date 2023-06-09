#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object inherited (directly or indirectly)
        from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object inherited (directly or indirectly)
    from the specified class;
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
