#!/usr/bin/python3

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.__objects = {}

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def get_objects(self):
        return self.__objects


    """
    # Test classes to use with the Storage class
    class SampleClass:
    def __init__(self, id_):
        self.id = id_


    def all(self):
        # return the dictionary __objects
        return self.__dict__

    def new(self, obj):
        # add obj to __objects with key <obj class name>.id
        pass

    def save(self):
        # serialize __objects to JSON and save to __file_path
        self.updated_at = datetime.datetime.now()

    def reload(self):
        # deserialize JSON file to __objects if file exists
        pass



    __nb_objects = 0

    def __init__(self, id=None):
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
        if id is None:
            BaseModel.__nb_objects += 1
            self.my_number = BaseModel.__nb_objects
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
        else:
            self.id = id
            self.class_type = self.__class__

    def __str__(self):
        """Override string to provide a better description."""
        # Create the ordered dictionary based on the desired order
        desired_order = ["my_number", "name", "__class__", "updated_at", "id", "created_at"]
        ordered_dict = {key: self.__dict__[key] for key in desired_order if key in self.__dict__}

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, ordered_dict)

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
    """



