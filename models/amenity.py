#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Features of the Space"""
    def __init__(self):
        super().__init__()
    name = ""
