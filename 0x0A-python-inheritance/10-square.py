#!/usr/bin/python3
class BaseGeometry:
    """Class representing base geometry."""


    def area(self):
        """Raises an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is an integer.

        Args:
            name: The name of the value being validated.
            value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Class representng a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width: The width of the rectangle.
            height: The height of the rectange.
        """
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns the rectangle descritpion.

            Returns:
                The rectangle description in the format
                [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size: The size of the square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns the square description.

        Returns:
            The square description in the format [square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
