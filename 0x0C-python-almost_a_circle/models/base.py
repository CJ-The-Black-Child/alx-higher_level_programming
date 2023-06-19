import json

class Base:
    """ Private class attribute to track the number of objects"""
    __nb_objects = 0

    def __init__(self, id=None):
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
