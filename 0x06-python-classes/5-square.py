#!/usr/bin/python3


class Square:
    """
    Class Square that defines a Square
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance
        Args:
        size (int): The size of the square (default is 0)
        Raises:
        TypeError: if size is not an integer
        ValueError: if size if less than 0
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
        value (int) : The size of the square
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
        Calculates and returns the are of the sqyare
            Returns:
        int: The area of the sqyare
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square witht the character '#'
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
