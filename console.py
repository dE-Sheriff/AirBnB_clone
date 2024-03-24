#!/usr/bin/python3
""" """
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """ """
    promt = "(sbnb)"
    
    def do_EOF(self, *args):
        """ """
        pass
        
    def do_quit(self, line):
        """ """
        pass

    def do_create(self, line):
        """ """
        pass
    def do_destroy(self, line):
        """ """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
