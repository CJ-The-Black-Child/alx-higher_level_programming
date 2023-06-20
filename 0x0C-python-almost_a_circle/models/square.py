#!/usr/bin/python3
"""Defines a Square model class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.

    Attributes:
        None

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
                               Defaults to 0.
            y(int, optional): The y-coordinate of the square's position.
                              Defaults to 0.
            id (int, optional): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary containing the square's attributes.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Varibale length argument list containing the
            attributes in the following order:
            - id
            - size
            - x
            - y
        **kwargs: Arbitraru keyword arguments for updating the attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )

    @staticmethod
    def from_dictionary(dict_repr):
        """
        Creates a Square instance from its dictionary representation.

        Args:
            dict_repr (dict): The dictionary representation of the square.

        Returns:
            Square: The Square instance created from the dictionary.
        """
        id = dict_repr.get('id')
        size = dict_repr.get('size')
        x = dict_repr.get('x', 0)
        y = dict_repr.get('y', 0)
        return Square(size, x, y, id)
