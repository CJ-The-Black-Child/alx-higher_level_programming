#!/usr/bin/python3
"""Class  Square that defines a square"""


class Square:
    """Class  Square that defines a square"""

    def __init__(self, size=0):
        """
        Initializes a square instance
        Args:
            size (int): The size of the square (default is 0)
        Raises:
            TypeERror: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns the are of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2
