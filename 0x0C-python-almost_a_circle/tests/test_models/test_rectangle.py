#!/usr/bin/python3

""" Module to test rectangle.py """

from io import StringIO
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests the Rectangle class """
    def test_init(self):
        """ tests the constructor """
        self.assertEqual(Rectangle(5, 8).width, 5)
        self.assertEqual(Rectangle(5, 10).height, 10)
        self.assertEqual(Rectangle(1, 2, 3).x, 3)
        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)
        with self.assertRaises(TypeError):
            Rectangle('hello', 2)
        with self.assertRaises(TypeError):
            Rectangle(2, 'hello')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 'hello')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 'hello')
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, -1)
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -2)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 3, -4)

    def test_area(self):
        """ test the area method """
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_str(self):
        """ test the __str__ magic method """
        rect = Rectangle(5, 5, 1, 2)
        output = '[Rectangle] ({}) 1/2 - 5/5'.format(rect.id)
        self.assertEqual(rect.__str__(), output)

    def test_display(self):
        """ tests the display method """
        output1 = "##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            Rectangle(2, 4).display()
            self.assertEqual(fake_output.getvalue(), output1)

        output2 = " ##\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            Rectangle(2, 4, 1).display()
            self.assertEqual(fake_output.getvalue(), output2)

        output3 = "\n ##\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            Rectangle(2, 4, 1, 1).display()
            self.assertEqual(fake_output.getvalue(), output3)

    def test_update(self):
        """ test the update method """
        rect = Rectangle(4, 5)
        rect.update()
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        rect.update(100)
        self.assertEqual(rect.id, 100)
        rect.update(100, 10)
        self.assertEqual(rect.width, 10)
        rect.update(100, 10, 12)
        self.assertEqual(rect.height, 12)
        rect.update(100, 10, 12, 3)
        self.assertEqual(rect.x, 3)
        rect.update(100, 10, 12, 3, 4)
        self.assertEqual(rect.y, 4)
        rect.update(20, 15, **{'x': 6})
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.x, 3)
        rect.update(**{'id': 1000})
        self.assertEqual(rect.id, 1000)
        rect.update(**{'id': 1000, 'width': 20})
        self.assertEqual(rect.width, 20)
        rect.update(**{'id': 1000, 'width': 20, 'height': 22})
        self.assertEqual(rect.height, 22)
        rect.update(**{'id': 1000, 'width': 20, 'height': 22, 'x': 5})
        self.assertEqual(rect.x, 5)
        rect.update(**{'id': 1000, 'width': 20, 'height': 22, 'x': 5, 'y': 2})
        self.assertEqual(rect.y, 2)

    def test_to_dictionary(self):
        """ test the to_dictionary method """
        output = {'id': 100, 'width': 5, 'height': 7, 'x': 2, 'y': 3}
        self.assertEqual(Rectangle(5, 7, 2, 3, 100).to_dictionary(), output)

    def test_create(self):
        """ test the create method """
        rect = Rectangle.create(**{'id': 1000})
        self.assertEqual(rect.id, 1000)
        rect = Rectangle.create(**{'id': 1000, 'width': 20})
        self.assertEqual(rect.width, 20)
        rect = Rectangle.create(**{'id': 1000, 'width': 20, 'height': 22})
        self.assertEqual(rect.height, 22)
        r = Rectangle.create(**{'id': 1000, 'width': 20, 'height': 22, 'x': 5})
        self.assertEqual(r.x, 5)
        dct = {'id': 1000, 'width': 20, 'height': 22, 'x': 5, 'y': 2}
        r = Rectangle.create(**dct)
        self.assertEqual(r.y, 2)
