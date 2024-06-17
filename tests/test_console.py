#!/usr/bin/python3
""" A class to test All files,
classes, functions using unit tests:
    HBNB_Testing_CommandPrompt
    HBNB_Testing_HelpCommand
    HBNB_Testing_ExitCommand
    HBNB_Testing_CreateCommand
    HBNB_Testing_ShowCommand
    HBNB_Testing_allCommand
    HBNB_Testing_destroyCommand
    HBNB_Testing_UpdateCommand
"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class HBNB_Testing_CommandPrompt(unittest.TestCase):
    """Unittests for testing prompt dsiplay of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(sbnb) ", HBNBCommand.prompt)


class HBNB_Testing_HelpCommand(unittest.TestCase):
    """Unittests for testing help command of the HBNB command interpreter."""

    def test_help_quit(self):
        msg = "Handle request to quit interpreter"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_EOF(self):
        msg = "Handles EOF characther(Exits)"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_create(self):
        msg = "Creates an instance of Basemodel"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_all(self):
        msg = "Prints all string format of stored instances"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(msg, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
