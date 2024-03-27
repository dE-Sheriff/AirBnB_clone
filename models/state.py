#!/usr/bin/python3
""" A state class Attribute """

from models.base_model import BaseModel


class State(BaseModel):
    """ Managing state class attributes """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State"""
        self.name = ""
        super(State, self).__init__(*args, **kwargs)
