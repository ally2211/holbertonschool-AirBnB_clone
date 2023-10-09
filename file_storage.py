#!/usr/bin/python3

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        # return the dictionary __objects
        pass

    def new(self, obj):
        # add obj to __objects with key <obj class name>.id
        pass

    def save(self):
        # serialize __objects to JSON and save to __file_path
        pass

    def reload(self):
        # deserialize JSON file to __objects if file exists
        pass
