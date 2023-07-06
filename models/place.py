#!/usr/bin/python3

from models.base_model import BaseModel

"""Module containing the Place
"""


class Place(BaseModel):
    """Place class that inherets from base model

    Args:
        BaseModel (class): parent class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]
