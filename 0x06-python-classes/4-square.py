#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """
        Initializes a Square instance
        Args:
            size (int): The size of the square (default is 0)
        Raises:
        TypeError: if size is nor an integer
        ValueError: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the value of size
        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of size
        Args:
            value (int): The size of the square
        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2
