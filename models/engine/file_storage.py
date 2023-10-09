#!/usr/bin/python3

"""
class desc file storage
"""
import json
import os
import datetime

class FileStorage:
    """
    filestorage methods
    """
    __file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'file.json')
    __objects = {}

    def __init__(self):
        self.__objects = {}
        self.__file_path = FileStorage.__file_path

    def all(self):
        # return the dictionary __objects
        return self.__dict__

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.__dict__
        
    def save(self):
        serializable_objects = {}
    
        for key, value in self.__objects.items():
            # Convert the object's dictionary to a serializable format
            obj_dict = value.copy()  # Assuming the value is a dictionary
            if 'created_at' in obj_dict and isinstance(obj_dict['created_at'], datetime.datetime):
                obj_dict['created_at'] = obj_dict['created_at'].isoformat()
            if 'updated_at' in obj_dict and isinstance(obj_dict['updated_at'], datetime.datetime):
                obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

            serializable_objects[key] = obj_dict

        with open(self.__file_path, 'w') as file:
            json.dump(serializable_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.__objects = {}
