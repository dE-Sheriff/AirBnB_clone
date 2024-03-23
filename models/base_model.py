#!/usr/bin/python3

import uuid
import datetime

class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        
    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
