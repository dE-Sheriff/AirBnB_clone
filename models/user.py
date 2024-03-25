#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """Class instance for User"""
    firs_name = ""
    last_name = ""
    email = ""
    password = ""
    
    def __init__(self, *args, **kwargs):
        """Initializes User"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super(User, self).__init__(*args, **kwargs)