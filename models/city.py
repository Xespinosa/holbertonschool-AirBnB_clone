#!/usr/bin/python3

from models.base_model import BaseModel

"""Module containing the City
"""


class City(BaseModel):
    """City class that inherets from base model

    Args:
        BaseModel (class): parent class
    """
    state_id = ""
    name = ""
