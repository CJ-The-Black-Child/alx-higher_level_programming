#!/usr/bin/python3
"""Student class definition"""


class Student:
    """Represents a class"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first name,
        last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the student instance to a JSON dictionary representation.

        Args:
            attrs (list, optional): A list of attribute name to
                                    include in the JSON dictionary.
                                    If None, all attributes will be included.

        Returns:
            dict: The JSON dictionary representation of the student instance.
            If attrs is provided, only the speicified attributes
            will be included in the dictionary.
        """
        if attrs is None:
            return self.__dict__

        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
                return json_dict
