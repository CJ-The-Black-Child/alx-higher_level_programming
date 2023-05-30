#!/usr/bin/python3
class Square:
    """
    Class Square that defines a square
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance
        Args:
        size (init): The size of the square (default is 0)
        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
