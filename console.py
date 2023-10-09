#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, line):
        """Exit the command interpreter"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
