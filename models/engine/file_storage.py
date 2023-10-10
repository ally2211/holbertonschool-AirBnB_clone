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
        """
        instantiates self
        """
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
        """
        returns all attributes in self
        """
        #print("in all")
        #if not self.__dict__:  # Check if the dictionary is empty
        if not os.path.exists(FileStorage.__file_path):
            return {} 
        else:
            return self.__dict__

    def new(self, obj):
        """
        creates new instance
        """
        #print("hello in new")
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.__dict__
        
    def save(self):
        """
        saves data to self obj
        """
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
        """
        reload reads json from file and stores it to self 
        """
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
        #print("reload")

        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                self.__objects = data
                self.__objects = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): 
            pass
            #self.__objects = {}
        
    def get(self, class_name, obj_id):
        """
        Retrieve one object based on its class and ID.
        """
        key = "{}.{}".format(class_name, obj_id)
        return self.__objects.get(key, None)
    
    def all_in_console(self, class_name=None):
        """Returns a dictionary of all objects, optionally filtered by class name."""
        if class_name:
            return {k: v for k, v in self.__objects.items() if class_name in k}
        return self.__objects

    def delete(self, class_name, obj_id):
        """Deletes an instance based on its class name and ID."""
        key = "{}.{}".format(class_name, obj_id)
        #print(f"Attempting to delete key: {key}")
        #print(f"Available keys: {self.__objects.keys()}")
        if key in self.__objects:
            del self.__objects[key]
