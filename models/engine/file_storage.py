#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """methods returns all dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as file:
                loaded_objects = json.load(file)

            for key, value in loaded_objects.items():
                class_name = value["__class__"]
                del value["__class__"]

                # Use globals() to access the global scope
                if class_name in globals():
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass


# Move this line outside the class definition
storage = FileStorage()
