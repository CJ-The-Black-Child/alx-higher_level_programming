#!/usr/bin/python3
"""Defines a Rectangle model class"""
from models.base import Base
import csv


class Rectangle(Base):
    """
    Represents a rectangle.

    Attributes:
        __nb_objects (int): Private class attribute to tract the number
                            of Rectangle objects.
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instances.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                               Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                                Deault to 0.
            id (int, optional): The id of the rectangle. Defaults to NOne.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is not None:
            self.id = id
        else:
            Rectangle.__nb_objects += 1
            self.id = Rectangle.__nb_objects

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing the rectangle's attributes.

        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    @property
    def width(self):
        """
        Get the width of the rectangle

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: if the height is not an integer.
            ValueError: If the height is less than or Equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinates of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-cordinates of the rectangle's position.

        Args:
            value (int): The x-coordinate of the rectangle's position.

        Raises:
            TypeError: If the x-coordinate is not an integer.
            ValueError: If the x-coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The y-coordinate of the rectangle's position.

        Raises:
            TypeError: If the y-coordinate is not an integer.
            ValueError: If the y-coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle using '#' characters.

        """
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable length argumnet list containing the attributes in
            the followig order:
                - id
                - width
                - height
                - x
                - y
            **kwargs: Arbitrary keyword arguments for updating the attributes.
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        if len(args) == 0 and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of Rectangle objects to a CSV file.

        Args:
            list_objs (list): A list of Rectangle objects.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                writer.writerow(row)
