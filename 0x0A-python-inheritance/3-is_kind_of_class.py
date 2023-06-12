#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or if inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class or if it
        inherited from it;
        False otherwise.
    """
    return isinstance(obj, a_class)
