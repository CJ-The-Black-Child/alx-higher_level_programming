#!/usr/bin/python3

class BaseGeometry:
    """Class representing base geometry."""

    def area(self):
        """Raises an exception indicating that area() is not implementing."""
        raise Exception("area() is not implmented")

    def integer_validator(self, name, value):
        """Validates that a value is an integer.

            Args:
                name: The name of the value being validated.
                value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an intger")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns the rectangle description.

        Returns:
            The rectangle description in the format
            [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Computes the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """Returns the square description.

        Retuns:
            The square description in the format
            [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
