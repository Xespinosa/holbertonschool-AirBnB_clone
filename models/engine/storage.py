#!/usr/bin/python
from models.base_model import BaseModel
import json

"""Module for File Storage management

Returns:
    dictionary: Dictionary saved on json file
"""


class FileStorage(BaseModel):
    """Class handling all file storage management

    Args:
        BaseModel (Class): Parent class

    Returns:
        dictionary : dictionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get the dictionary that has been created

        Returns:
            Dictionary: all objects
        """
        return self.__objects

    def new(self, obj):
        """add a new object to the dectionary

        Args:
            obj (any): object to be saved on dictionary
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """save object dictionary to json file
        """
        object_dict = {}
        for key, value in self.__objects.items():
            object_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(object_dict, f)

    def reload(self):
        """unload json file dictionary to object dictionary completely
        """
        if self.__file_path:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                json_data = json.load(f)
            self.__objects = {}
            for key, value in json_data.items():
                self.__objects[key] = BaseModel(**value)
