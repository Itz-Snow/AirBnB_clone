#!/usr/bin/python3

""" information on the following imports
1.  import cmd: module to have commandline
features for testing code and backend services
2. import BaseModel: For creating instances from
    the interpreter
3. import FileStorage: for storing information into local JSON
    file
4. import User: for creating user instances
5. import Review: instances for reviewing an home
6. import City: for creating instances of city
7. import Place
8. import Amenity: for creating instances of amenities in each home
9. import State: class for placing the state homes are located at
"""

import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage as file
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City


class HBNBCommand(cmd.Cmd):
    """ AirBnb cmd class for AirBnb project clone """

    prompt = "(hbnb) "

    def do_all(self, arg):
        """ Prints all instances of a class name (if provided)
        or all created instances if class name is not specified
        """
        storage.reload()
        db = storage.all()
        result = []
        if arg:
            if arg in globals():
                for key in db.keys():
                    text_split = key.split(".")
                    classname = text_split[0]
                    if arg == classname:
                        new_key = "{}.{}".format(classname, text_split[1])
                        data = str(db[new_key])
                        result.append(data)
                print(result)
            else:
                print("** class doesn't exist **")
        else:
            for key in db.keys():
                data = str(db[key])
                result.append(data)
            print(result)

    def do_create(self, arg):
        """ creates an instance of BaseModel and saves to JSON file
        then prints the id """
        if arg:
            if arg in globals():
                base_model = globals()[arg]()
                base_model.save()
                print(base_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ deletes an instance from the local storage """
        storage.reload()
        db = storage.all()
        result = []
        if arg:
            split_arg = arg.split()
            if len(split_arg) == 2:
                if split_arg[0] in globals():
                    class_key = ".".join(split_arg)
                    print(class_key)
                    if class_key in db:
                        del db[class_key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(split_arg) < 2:
                if split_arg[0] not in globals():
                    print("** class doesn't exist **")
                elif split_arg[0] in globals():
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_EOF(self, arg):
        """ exits program at the end of file (EOF) """
        sys.exit(1)

    def do_update(self, arg):
        """updates an instance based on the class name and id
        Methodology: Create a new instance and setting the value
        to the instance"""
        storage.reload()
        db = storage.all()
        if arg:
            text_split = arg.split()
            if len(text_split) >= 4:
                key = text_split[2]
                value = text_split[3]
                if text_split[0] in globals():
                    keys = "{}.{}".format(text_split[0], text_split[1])
                    if keys in db:
                        try:
                            str_value = str(value)
                            setattr(db[keys], key, value)
                        except TypeError:
                            try:
                                float_value = float(value)
                                setattr(db[keys], key, value)
                            except TypeError:
                                try:
                                    int_value = int(value)
                                    setattr(db[keys], key, value)
                                except TypeError:
                                    pass
                        finally:
                            storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(text_split) == 1:
                print("** instance id missing **")
            elif len(text_split) == 2:
                print("** attribute name missing **")
            elif len(text_split) == 3:
                print("** value missing **")

        else:
            print("** class name missing **")

    def emptyline(self):
        """ Prevents the execution of the previous command
        when enter ↵ is pressed on an emptyline"""
        pass

    def do_quit(self, arg):
        """ exit the interpreter by typing quit"""
        sys.exit(0)

    def do_show(self, arg):
        """ print the string representation of an instance based
        on the class name and id """
        if arg:
            storage.reload()
            db = storage.all()
            text_split = arg.split()
            if len(text_split) <= 1:
                print("** instance id missing **")
            elif len(text_split) >= 2:
                class_name = text_split[0]
                class_id = text_split[1]
                if class_name in globals():
                    db_key = "{}.{}".format(class_name, class_id)
                    if db_key in db:
                        print(db[db_key])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def help(self):
        """ prints the help functions for the cmd class """


if __name__ == "__main__":
    HBNBCommand().cmdloop()