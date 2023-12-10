#!/usr/bin/python3
import cmd
import shlex
from models import base_model

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Review", "Place"]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) signal to exit the program."""
        return True

    def emptyline(self):
        pass

    def help(self, arg):
        if not arg:
            super().do_help("")
        else:
            try:
                getattr(self, "help_{}".format(arg))
            except AttributeError:
                print("No help available for this command.")
if __name__ == "__main__":
    HBNBCommand().cmdloop()
