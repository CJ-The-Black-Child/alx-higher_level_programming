#!/usr/bin/python3
"""Defines a class that is BaseGeometry."""


class BaseGeometry:
    """Class representing base geomtry."""

    def area(self):
        """Raises an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
