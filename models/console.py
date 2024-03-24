#!/usr/bin/python3
""" """
import cmd
import sys

class SBNBcommand(cmd.Cmd):
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

if __name__ == "__maina__":
    SBNBcommand().cmdloop()
