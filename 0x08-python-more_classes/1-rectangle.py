#!/usr/bin/python3
"""Defines a Rectangle class"""

class Rectangle:
    """
    Rectangle class represents a rectangle object with width
    and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with the specified width and height.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.__width = 0
        self.__height = 0
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectabgle.

        Returns:
            int: Height of the rectangle.
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
