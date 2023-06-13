#!/usr/bin/python3
"""
A student class represeting a student with attributes and JSON serialization.
"""


class Student:
    """
        define a class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Convert the student object to a JSON-serializable dictionary.

        Returns:
            dict: A dictionary representing the student object in JSON format.
        """
        serializable_dict = {
            'first_name': self.first_name,
            'last_name':  self.last_name,
            'age': self.age
        }
    return serializable_dict
