#!/usr/bin/python3
"""
A class representing a student with attributes
and methods for JSON serialization.
"""


class Student:
    """defines a class student"""
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with the provided first name,
        last name and age.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the Student object to a JSON dictionary.

        if `attrs` is None, it returns a dictionary representation of
        the entire object.
        if `arres` is a list of attribute names, it returns a dictionary
        containing only the specified attributes.

        Args:
            attrs (list): A list of attribute names (optional).

        Returns:
            dict: A dictionary representation of the student object.
        """

        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
                return json_dict

    def reload_from_json(self, json):
        """
        Reloads the student object from a JSON dictionary.

        Updates the attributes of the stident object with the key-value pairs
        provided JSON dictionary.

        Args:
            json (dict): A dictionary representin a JSON object
                         containing the student attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
