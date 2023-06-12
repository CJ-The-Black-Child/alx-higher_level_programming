#!/usr/bin/python3
"""Defines a base class: BaseGeometry."""


class BaseGeometry:
    """Class representing base geometry."""

    def integer_validator(self, name, value):
        """Validates if a value is an integer greater than 0.

        Args:
            name: The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
