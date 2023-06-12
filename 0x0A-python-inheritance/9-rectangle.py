#!/usr/bin/python3

class BaseGeometry:
    """Class representing base geometry."""

    def area(self):
        """Raises an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is an integer greater than 0.

            Args:
                name: The name of the value being validated.
                value: The value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width: The width of the rectnagle.
            height: The height of the rectangle.
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

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height
