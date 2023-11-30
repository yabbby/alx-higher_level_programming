#!/usr/bin/python3
"""
    Module to test max_integer function
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class MaxIntegerTest(unittest.TestCase):
    """
    TestCase subclass with tests for max_integer function
    """

    def test_correct_max_value(self):
        """
        test valid inputs
        """
        test_list = [3, 13, 24, 36, 9, 33, 19]
        self.assertEqual(max_integer(test_list), 36)
        self.assertEqual(max_integer([4.3, 4.15, 4.25]), 4.3)
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")
        self.assertEqual(max_integer([4.15, 4.3, 4.25]), 4.3)

    def test_empty_input(self):
        """
        test empty input
        """
        self.assertEqual(max_integer([]), None)

    def test_invalid_input(self):
        """
        test invalid inputs
        """
        with self.assertRaises(TypeError):
            max_integer(None)
            max_integer(["a", 2, 2.5])
            max_integer([[1, 2], 6])
            max_integer([{1, 2}, 6])


if __name__ == "__main__":
    unittest.main()
