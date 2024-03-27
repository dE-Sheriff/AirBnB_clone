#!/usr/bin/python3
"""Implementing the Place class Attribute"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = ""
    number_bathroom = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
