#!/usr/bin/python3
"""Class Square defining a square"""


class Square:
    """
    Class Square that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Sqaure instance
        Args:
        Size (int): The size of the square (default is 0)
        Position (tuple): The posiition of the square (default is 0, 0)
        Raises:
        TypeError: if size is not an integer or position is
        not a tuple of 2 positive integers
        ValueError: if size is less than 0 or position contains negative
        values
        """

        self.size = size
        self.position = position

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
            Value (int): The size of the square
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

    @property
    def posiiton(self):
        """
        Retrieves the value of position
        Returns:
        tuple: The position if the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the value of position
        Args:
            value (tuple): The position of the square
        Raises:
        TypeError: if value is not a tuple of 2 positive integers
        ValueError: if value contains negative values
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TyprError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value) \
                or any(num < 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square
        Returns:
        int: The area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the char '#'
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
