#!/usr/bin/python3

from models.base_model import BaseModel

"""Module containing the Review
"""


class Review(BaseModel):
    """Review class that inherets from base model

    Args:
        BaseModel (class): parent class
    """
    place_id = ""
    user_id = ""
    text = ""
