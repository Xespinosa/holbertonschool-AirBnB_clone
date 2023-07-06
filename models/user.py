#!/usr/bin/python3

from models.base_model import BaseModel

"""Module containing the user
"""


class User(BaseModel):
    """user class that inherets from base model

    Args:
        BaseModel (class): parent class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
