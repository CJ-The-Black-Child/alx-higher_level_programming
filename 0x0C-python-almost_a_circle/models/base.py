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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            obj_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_list)
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            """Create a dummy Rectangle instance"""
        elif cls.__name__ == "Square":
            dummy = cls(1)
            """Create a dummy square instance"""
        dummy.update(**dictionary)
        """Apply the real values using the update method"""
        return dummy
