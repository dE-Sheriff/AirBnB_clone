#!/usr/bin/python3
""" The file storage system for SBNB files"""
import json
import os
import datetime


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a string of the __object dictionary"""
        return self.__objects

    def save(self):
        """serializes __objects to the JSON file"""
        objt_dic = {}
        for key in self.__objects.keys():
            if type(self.__objects[key]) is not dict:
                objt_dic[key] = self.__objects[key].to_dicct()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, f)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def reload(self):
        """ Reloads stored objects/BaseModels """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dic = json.load(f)
            obj_dic = {k: self.classes()[v["__class__"]](**v)
                       for k, v in obj_dic.items()}

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
