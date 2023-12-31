#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""Module for the AirBnB Clone
"""


class BaseModel:
    """Class Base Model
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialization method that either reassigns values from a given
        dictionary or assigns the values correctly for the first time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:
            models.storage.new(self)

    def __str__(self):
        """Method to return a string containing public instance attributes

        Returns:
            String: string representation of all public instance attributes
        """
        name = self.__class__.__name__
        idcpy = self.id
        dct = self.__dict__
        return f"[{name}] ({idcpy}) <{dct}>"

    def save(self):
        """Method to save when the instance has been updated and save to json
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Save the Instance to dictionary

        Returns:
            dictionary: dictionary containing all public instance attributes
        """
        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = self.__class__.__name__
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        dict_cpy["created_at"] = self.created_at.isoformat()
        return dict_cpy
