#!/usr/bin/python3
"""import models"""
from unittest import TestCase
from unittest.mock import patch
import unittest
from io import StringIO
from console import HBNBCommand
from models import storage


class Test_Console(TestCase):
    """Test console"""

    def test_Prompte(self):
        """Test promple"""
        a = HBNBCommand.prompt
        self.assertEqual("(hbnb) ", a)

        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
<<<<<<< HEAD
            self.console.onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())

    def test_userall_command_output(self):
        """tests the user.all command output"""
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
<<<<<<< HEAD
                self.assertFalse(HBNBCommand().onecmd("create {}".format(cls))
                output = f.getvalue().strip()
                """check print id"""
                self.assertRegex(output, a)
                """ckeck if key of object is exist"""
                Cls_id = f"{cls}.{output}"
                self.assertIn(Cls_id, storage.all().keys())

    def test_ShowCommand(self):
        """test show command"""
        """test Doc"""
        all_Classes = ["BaseModel", "User", "City",
                       "Place", "Review", "State", "Amenity"]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue()
            """test help shold print:"""
            doc = "Prints the string representation of an instance\n"
            self.assertEqual(doc, output)

            """shold not exit program"""
            self.assertFalse(HBNBCommand().onecmd("help show"))

        """test ** class name missing **"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            output = f.getvalue()
            self.assertEqual("** class name missing **\n", output)

        """test ** class doesn't exist **"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show XXXX"))
            output = f.getvalue()
            self.assertEqual("** class doesn't exist **\n", output)

        """** instance id missing **"""
        for Cls in all_Classes:
=======
                console.HBNBCommand().onecmd("{}.all()".format(test_class))
                output = f.getvalue()
            self.assertIn(test_class, output)
            self.assertIn("created_at", output)
=======
            HBNBCommand().onecmd("")
            output = f.getvalue()
            self.assertEqual("", output)
>>>>>>> d3e0bf5de4d99c239c7d8a108d7c92a891ed6c02

    def test_HelpCommand(self):
        """test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            """test help shold print:"""
            doc = "Documented commands (type help <topic>):"
            doc2 = "========================================"
            doc3 = "EOF  all  count  create  destroy  help  quit  show  update"
            self.assertIn(doc, output)
            self.assertIn(doc2, output)
            self.assertIn(doc3, output)

            """shold not exit program"""
            self.assertFalse(HBNBCommand().onecmd("help"))

            """test help shold't print:"""
            docer = "Undocumented commands:"
            self.assertNotIn(docer, output)

    def test_QuitCommand(self):
        """test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()

            """test help shold print:"""
            doc = "quit to EXIT The program\n"
            self.assertEqual(doc, output)

            """shold not exit program"""
            self.assertFalse(HBNBCommand().onecmd("help quit"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOFCommand(self):
        """test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
<<<<<<< HEAD
            self.console.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_update(self):
        """Test cmd output: update"""
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
>>>>>>> 38892db2f8f4a4e4cfe0e11cd7d794d7269d40cd
            with patch('sys.stdout', new=StringIO()) as f:
                console.HBNBCommand().onecmd("create {}".format(test_class))
                obj_id = f.getvalue()
                cmd = "update {} {} name hbnb".format(test_class, obj_id)
                console.HBNBCommand().onecmd(cmd)
                cmd3 = "{}.update({}, first_name, alxhbnb\
                                  )".format(test_class, obj_id)
                console.HBNBCommand().onecmd(cmd3)
                cmd4 = "{}.update({}, last_name, alxholberton\
                                  )".format(test_class, obj_id)
                console.HBNBCommand().onecmd(cmd4)
                console.HBNBCommand().onecmd("show {} {}".format
                                             (test_class, obj_id))
                output = f.getvalue()
            self.assertIn("'name': 'hbnb'", output)
            self.assertIn("'first_name': 'alxhbnb'", output)
=======
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue()

            """test help shold print:"""
            doc = "Ctrl+d To EXIT The program\n"
            self.assertEqual(doc, output)
>>>>>>> d3e0bf5de4d99c239c7d8a108d7c92a891ed6c02

            """shold not exit program"""
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_CreateCommand(self):
        """test create command"""
        """test Doc"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue()
            """test help shold print:"""
            doc = "Creates a new instance of BaseModel, and prints the id\n"
            self.assertEqual(doc, output)

            """shold not exit program"""
            self.assertFalse(HBNBCommand().onecmd("help create"))

        """test ** class name missing **"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            output = f.getvalue()
            self.assertEqual("** class name missing **\n", output)

        """test ** class doesn't exist **"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create XXXX"))
            output = f.getvalue()
            self.assertEqual("** class doesn't exist **\n", output)

        all_Classes = ["BaseModel", "User", "City",
                       "Place", "Review", "State", "Amenity"]
        a = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab]' \
            r'[0-9a-f]{3}-[0-9a-f]{12}$'

        for cls in all_Classes:
            """test models"""
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {cls}"))
                output = f.getvalue().strip()
                """check print id"""
                self.assertRegex(output, a)
                """ckeck if key of object is exist"""
                Cls_id = f"{cls}.{output}"
                self.assertIn(Cls_id, storage.all().keys())

    def test_ShowCommand(self):
        """test show command"""
        """test Doc"""
        all_Classes = ["BaseModel", "User", "City",
                       "Place", "Review", "State", "Amenity"]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue()
            """test help shold print:"""
            doc = "Prints the string representation of an instance\n"
            self.assertEqual(doc, output)

            """shold not exit program"""
            self.assertFalse(HBNBCommand().onecmd("help show"))

        """test ** class name missing **"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            output = f.getvalue()
            self.assertEqual("** class name missing **\n", output)

        """test ** class doesn't exist **"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show XXXX"))
            output = f.getvalue()
            self.assertEqual("** class doesn't exist **\n", output)

        """** instance id missing **"""
        for Cls in all_Classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"show {Cls}"))
                output = f.getvalue()
                self.assertEqual("** instance id missing **\n", output)


if __name__ == "__main__":
    unittest.main()
