#!/usr/bin/python3
"""
This module defines the Base class and its associated methods for managing
objects.
"""

import json
import turtle
import csv


class Base:
    """ Private class attribute to track the number of objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes a new Base instance.
            Args:
                id (int, optional): The Id of the object. Defaults to None.
        """
        if id is not None:
            """
            If id is provided, assign it to the public instance
            attribute
            """
            self.id = id
        else:
            """
            Increment __nb_objects and assign the new value to the public
            instance attribute
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries
                                      representing objects.
        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.
        """
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            obj_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_list)
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representation of a
                               list dictionaires.
        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance using a dictionary of attributes.

        Args:
            dictionary (dict): A dictionary containing the attributes
                               of the object.

        Returns:
            Base: A new instance of the Base class with the given attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            """Create a dummy Rectangle instance"""
        elif cls.__name__ == "Square":
            dummy = cls(1)
            """Create a dummy square instance"""
        dummy.update(**dictionary)
        """Apply the real values using the update method"""
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                obj_dicts = cls.from_json_string(json_str)
                instances = [cls.create(**obj_dict) for obj_dict in obj_dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be saved.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads a list of instances from a CSV file.

        Returns:
            list: A list of instances loaded from the file.

        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, row[:5])
                        from models.rectangle import Rectangle
                        instance = Rectangle(width, height, x, y, id)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row[:4])
                        from models.square import Square
                        instance = Square(size, x, y, id)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """
        Draws rectangles and squares on a graphics window.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.
        """
        turtle.setup(800, 600)
        turtle.title("Rectangles and Squares")
        turtle.speed(2)

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendow()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()
