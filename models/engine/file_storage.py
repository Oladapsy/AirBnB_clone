#!/usr/bin/python3
""" this is a class that defines file storage"""
from models.basemodel import BaseModel
import os


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

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        ob = "obj.__class__.__name__"
        FileStorage.__objects[f"{ob}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        fname = "FileStorage.__file_path"
        fobj = "FileStorage.__objects"
        with open(filename='fname', mode='w', unicode='utf-8') as file:
            newdict = {}
            for k, v in fobj.items():
                newdict[k] = v.to_dict()
            file.write(json.dumps(newdict))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        fname = "FileStorage.__file_path"
        try:
            with open(filename='fname', mode='r') as file:
                objdict = json.load(file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))

        except FileNotFoundError:
            return
