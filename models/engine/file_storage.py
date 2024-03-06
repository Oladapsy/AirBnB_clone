#!/usr/bin/python3
""" this is a class that defines file storage"""
from models.basemodel import BaseModel

class FileStorage:
    """ class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ a public instance method all that returns the dictionary
        object(private)
        """
        return FileStorage.__objects

    def new(self):
        """ sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{} {}"]

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """


