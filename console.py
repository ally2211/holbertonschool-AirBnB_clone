#!/usr/bin/env python3
"""
this is a shell in python
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    A simple command interpreter for the AirBnB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit the program.
        """
        exit()

    def do_EOF(self, args):
        """
        Quit the program.
        """
        self.do_quit(args)

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def all(self):
        """
        get all attributes
        """
        BaseModel.all()

    def do_create(self, line):
        """
        Create a new instance of BaseModel, save it to JSON file, and print its id.
        Usage: create BaseModel
        """
        if not line:  # check if there's no class name provided
            print("** class name missing **")
            return

        if line != "BaseModel":
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = line.split()

        # Check if class name is provided
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        # Check if class name is valid
        if class_name != "BaseModel": 
            print("** class doesn't exist **")
            return

        # Check if id is provided
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]

        # Attempt to retrieve the object
        # assumes `storage.get(class_name, obj_id)` exists that returns None if not found
        obj = storage.get(class_name, obj_id)

        if obj is None:
            print("** no instance found **")
            return

        # Print the dictionary representation of the object
        print(obj)

    def do_all(self, line):
        """
        Prints the string representation of all instances based or not on the class name.
        """
        args = line.split()

        if len(args) == 0:
            # Print all instances
            objs = storage.all_in_console(BaseModel)
        else:
            class_name = args[0]
            # Validate the class name
            if class_name != "BaseModel":  # you can expand this check for other classes as needed
                print("** class doesn't exist **")
                return
            
            # Get all instances of the specified class
            objs = storage.all_in_console(class_name)
            # Convert the objects to their string representations
            string_reprs = [str(obj) for obj in objs.values()]

            # Print the list of string representations
            print(string_reprs)

    def do_destroy(self, line):
        """
        Deletes an instance based on its class name and ID and saves the change into the JSON file.
        Usage: destroy <class name> <id>
        """
        args = line.split()

        # If the class name is missing
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        # Check if the class name doesn't exist (you might need to adjust this depending on available classes)
        valid_classes = ["BaseModel"]  # Add other class names to this list if needed
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        # If the id is missing
        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_id = args[1]

        # If the instance of the class name doesn't exist for the id
        key = "{}.{}".format(class_name, obj_id)
        storage.delete(class_name, obj_id)
        #obj = storage._FileStorage__objects[key]
        #print("** no instance found **")
        #if key in storage._FileStorage__objects:
        #    del storage._FileStorage__objects[key]
        #else:
        #    print("** no instance found **")


    def do_update(self, line):
        args = line.split()

        # Check for missing arguments and print error messages
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel"]:  # Add other valid class names to the list
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        class_name, obj_id, attr_name, attr_value = args[0], args[1], args[2], args[3]

        # Remove double quotes from the attribute value
        attr_value = attr_value.strip("\"")

        key = "{}.{}".format(class_name, obj_id)
        obj = storage._FileStorage__objects[key]
        if key not in obj:
            print("** no instance found **")
            return

        obj = storage.__objects[key]

        # Ensure we're not updating a protected attribute
        if attr_name in ["id", "created_at", "updated_at"]:
            return

        # Convert attribute value to the correct type if needed
        try:
            if "." in attr_value:  # This could be a float
                value = float(attr_value)
            else:
                value = int(attr_value)
        except ValueError:
            value = attr_value  # Just a string

        setattr(obj, attr_name, value)
        obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
