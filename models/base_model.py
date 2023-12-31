#!/usr/bin/python3
"""
Module Doc: Base Class for all other classes
"""
import json
import datetime
import uuid
from models import storage


class BaseModel:
    """
    class Doc: Base Class
    """
    __nb_objects = 0

    def __init__(self, *args, **kwargs):
        """
        function Desc:  init
        """

        if kwargs:
            # Initialization when 'id' is provided in keyword arguments
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        dv = datetime.datetime.strptime(value, date_format)
                        setattr(self, key, dv)
                    else:
                        setattr(self, key, value)
        else:
            BaseModel.__nb_objects += 1
            self.my_number = BaseModel.__nb_objects
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
            storage.new(self)
            
            """
            # Create the ordered dictionary based on the desired order

            selfdesired_order = ["id", "created_at", "my_number",
            "updated_at", "name"]
            selfordered_dict = {}

            for key in selfdesired_order:
                if key in self.__dict__ and key != "__class__":
                    selfordered_dict[key] = self.__dict__[key]
            self.__dict__ = selfordered_dict
            """

    def __str__(self):
        """
        Override string to provide a better description.
        """
        print("__str__ in basemodel")
        # Create the ordered dictionary based on the desired order
        desired_order = ["my_number", "name",  "__class__", "updated_at", "id",
                         "created_at"]
        ordered_dict = {key: self.__dict__[key] for key in desired_order
                        if key in self.__dict__}

        return f"[{self.__class__.__name__}]({self.id}){ordered_dict}"

    def save(self):
        """
        update public instance attribute updated_at by current datetime
        """
        #print("save in basemodel")
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return dictionary contains keys/values, __dict__, the instance 
        """
        print("to dict method")
        dict_rep = self.__dict__.copy()
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        # Add the class type
        dict_rep['__class__'] = self.__class__.__name__

        desired_order = ["my_number", "name", "__class__", "updated_at",
                         "id", "created_at"]
        ordered_dict = {key: dict_rep[key] for key in desired_order
                        if key in dict_rep}
        return ordered_dict
