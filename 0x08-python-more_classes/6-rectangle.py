#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with the specified width and height.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self.width

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
            raise TypeError("width must be an integer.")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: height of the rectangle.
        """
        return self.__height

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
            raise TypeError("height must be an integer.")
        if value < 0:
            raise ValueError("height must be >= 0")
            self.__height = value

    def area(self):
        """
        Calculates and returns the are of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle,
            with '#' characters forming the shape.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(['#' * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used
        to recreate a new instance of the rectangle using eval().

        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        Decrements the count of instances of Rectangle.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
