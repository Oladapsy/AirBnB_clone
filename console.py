#!/usr/bin/python3
"""A program that contains entry point of the command interpreter: """
import cmd


class HBNBCommand(cmd.Cmd):
    """The command line for the programm... powered by cmd"""
    prompt = '(hbnb) '
    def do_EOF(self, line):
        """The end of file which uses Ctrl D to quit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """should do nothing when the line is empty"""
        return False

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        return True





if __name__ == '__main__':
    HBNBCommand().cmdloop()
