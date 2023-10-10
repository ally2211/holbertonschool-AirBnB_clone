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
        #self.__file_path = FileStorage.__file_path
        #print("hello im in filestorage init")
    """
    def all(self):
        # return the dictionary __objects
        #print("hello in all")
        return self.__dict__
    """

    def all(self):
        #if not self.__dict__:  # Check if the dictionary is empty
        if not os.path.exists(FileStorage.__file_path):
            return {} 
        else:
            return self.__dict__

    def new(self, obj):
        #print("hello in new")
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.__dict__
        
    def save(self):
        #print("hello in save")
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
        #print("hello in reload")
        """Deserializes the JSON file to __objects
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    # Convert string representation back to datetime objects
                    if 'created_at' in value:
                        value['created_at'] = datetime.datetime.fromisoformat(value['created_at'])
                    if 'updated_at' in value:
                        value['updated_at'] = datetime.datetime.fromisoformat(value['updated_at'])

                    class_name, obj_id = key.split('.')
                
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        """ 
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                self.__objects = data
                self.__objects = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): 
            pass
            #self.__objects = {}
        
        
