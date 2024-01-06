#!/usr/bin/python3

""" Module to test base.py """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ class to test base.py """
    def test_init(self):
        b1 = Base()
        self.assertTrue(b1.id == 1)
        b2 = Base()
        self.assertTrue(b2.id == 2)
        b3 = Base(100)
        self.assertTrue(b3.id == 100)
        b4 = Base()
        self.assertTrue(b4.id == 3)

    def test_to_json_string(self):
        """ test the to_json_string method """
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        jst = Base.to_json_string([{'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}])
        self.assertEqual(jst, '[{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5}]')

    def test_from_json_string(self):
        """ test the from_json_string method """
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string(None), [])
        jst = '[{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5}]'
        lst = Base.from_json_string(jst)
        self.assertEqual(lst, [{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5}])
