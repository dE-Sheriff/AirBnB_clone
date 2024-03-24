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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dic = {k: v.to_dict() for k,
                                  v in FileStorage.__objects.items()}
            json.dump(dic, f)
    
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def reload(self):
        if FileStorage.__file_path is None:
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dic = json.load(f)
            obj_dic = {k: self.classes()[v["__class__"]](**v)
                       for k, v in obj_dic.items()}
