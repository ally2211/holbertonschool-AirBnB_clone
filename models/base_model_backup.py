#!/usr/bin/python3
"""
Module Doc: Base Class for all other classes
"""
import json
import datetime
import uuid


class BaseModel:
    """
    class Doc: Base Class
    """
    __nb_objects = 0

    def __init__(self, *args, **kwargs):
        """
        function Desc:  init
        """
        if id is None:
            BaseModel.__nb_objects += 1
            self.my_number = BaseModel.__nb_objects
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
        

        elif "id" in kwargs:
            # Initialization when 'id' is provided in keyword arguments
            date_format = "%Y-%m-%dT%H:%M:%S.%f"

            for key, value in kwargs.items():
                if key == "my_number" and not isinstance(value, (int, type(None))):
                    # This will raise an error if id is not an integer or None
                    raise ValueError("id must be an integer or None")
                if hasattr(self, key):
                    if key != "__class__":
                        setattr(self, key, value)           
                        print("{}".format(self.id))

            self.created_at =  datetime.datetime.strptime(kwargs['created_at'], date_format)
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], date_format)
            # Create the ordered dictionary based on the desired order
            """
            selfdesired_order = ["id", "created_at", "my_number","updated_at", "name"]
            selfordered_dict = {}
            
            for key in selfdesired_order:
                if key in self.__dict__ and key != "__class__":
                    selfordered_dict[key] = self.__dict__[key]
            
            self.__dict__ = selfordered_dict
            """
            """
            id = getattr(self, "id", None)
            if hasattr(self, "id"):
                id = self.id
            else:
                id = None
            """
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
            """ 
            self.__dict__.values()
            return used in task3 - keeping for now
            return "[{}] ({}) {}".format(self.__class__.__name__, self.id, ordered_dict)
            """

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        dict_rep = self.__dict__.copy()
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        # Add the class type
        dict_rep['__class__'] = self.__class__.__name__

        desired_order = ["my_number", "name", "__class__", "updated_at", "id", "created_at"]
        ordered_dict = {key: dict_rep[key] for key in desired_order if key in dict_rep}
        return ordered_dict

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        desired_order = ["y", "x", "id", "width", "height"]
    
        # Check for None or empty list first
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
    
        # Order each dictionary in the list
        ordered_list = []
        for d in list_dictionaries:
            ordered_data = {key: d[key] for key in desired_order if key in d}
            ordered_list.append(ordered_data)
    
        return json.dumps(ordered_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        """
        filename = cfilename = cls.__name__ + ".json"
        list_to_store = []
    
        if list_objs is not None:
            list_to_store = [obj.to_dictionary() for obj in list_objs]
    
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_to_store))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string:
        """
        if json_string is None or not json_string:
            return "[]"
        else:
            # Deserialize the JSON string into a list of dictionaries
            list_of_dicts = json.loads(json_string)

            desired_order = ["height", "width", "id"]

            # Order each dictionary in the list
            ordered_list = []
            for d in list_of_dicts:
                ordered_data = {key: d[key] for key in desired_order if key in d}
                ordered_list.append(ordered_data)

            return json.dumps(ordered_list)

    @classmethod
    def load_from_file(cls):
        """
        returns list of instances
        """
        fileoutput = cls.__name__ + ".json"

        with open(fileoutput, 'r') as file:
            content = file.read()
        list_output = cls.from_json_string(content)

        instances = []
        for dictionary in list_output:
            if isinstance(dictionary, dict):
                instance = cls.create(**dictionary)
                instances.append(instance)
        return instances
