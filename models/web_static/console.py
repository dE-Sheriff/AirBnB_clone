#!/usr/bin/python3

"""AirBnB project command line module"""

import cmd
import sys
import json
import re
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBnB project command line interpreter"""
    prompt = "(sbnb)"
    
    def check_line(self, line):
        """Checks if line is missing a command"""
        if line is None or line == "":
            print("** class name missing **")
            return
        
    def _precmd(self, line):
        """ Makes interpreter accessible
        even in non_interactive mode"""
        match = re.search(r"^(\w*)\.(\w+)(?:\
            (([^)]*)\))$", line)
        if not match:
            return line
        name = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_id_and_args = re.research('^"([^"]*)"(?:,(.*))?$', args)
        
        if match_id_and_args:
            id = match_id_and_args.group(2)
        else:
            id = args
            attr_or_dict = False
        
        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.research('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(name, id, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            
            command = method + " " + name + " " + id + " " + attr_and_value
            self.onecmd(command)
            return command
        
    def do_EOF(self, *args):
        """Handles EOF characther"""
        print()
        return True
        
    def do_quit(self, line):
        """ Handle request to quit interpreter"""
        return True

    def do_create(self, line):
        """Command to create an instance"""
        self.check_line(line=line)
        if line not in storage.classes():
            print("** class doesn't exist **")
        else:
            sel_class = storage.classes()[line]()
            sel_class.save()
            print(sel_class.id)
        
    def do_destroy(self, line):
        """Deletes specified instance stored"""
        self.check_line(line=line)
        words = line.split(" ")
        if words[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(words[0], words[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
    
    def do_all(self, line):
        """Prints all stored instances"""
        self.check_line(line)
        words = line.split(' ')
        if words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            nl = [str(obj) for key, obj in storage.all().items()
                if type(obj).__name__ == words[0]]
            print(nl)
    
    def do_count(self, line):
        """Counts number of stored instances"""
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
