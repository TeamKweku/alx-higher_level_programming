#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ checking specific test.
    """
    def test_empty(self):
        """check if empty."""
        lst = []
        self.assertEqual(max_integer(lst), None)

    def test_sorted(self):
        """checks for max when sorted."""
        lst = [5, 6, 7, 8]
        self.assertEqual(max_integer(lst), 8)

    def test_sorted_descending(self):
        """checks for max when sorted."""
        lst = [8, 7, 6, 5]
        self.assertEqual(max_integer(lst), 8)

    def test_unsorted(self):
        """checks for max when list is not sorted."""
        lst = [2, 78, -1, 5]
        self.assertEqual(max_integer(lst), 78)

    def test_all_negative(self):
        """checks for max when all values are negative."""
        lst = [-1, -7, -5, -6]
        self.assertEqual(max_integer(lst), -1)

    def test_onlyone(self):
        """checks for max when their is only one element."""
        lst = [5]
        self.assertEqual(max_integer(lst), 5)

    def test_floats(self):
        """checks for max when all values are floats."""
        lst = [5.6, 7.6, 1.4, 6.8]
        self.assertEqual(max_integer(lst), 7.6)

    def test_mixofintandfloat(self):
        """checks for max when values are floats and ints."""
        lst = [5.6, 7.6, 5, 8, 7.4]
        self.assertEqual(max_integer(lst), 8)

    def test_string(self):
        """checks for max when its a string."""
        lst = "string"
        self.assertEqual(max_integer(lst), 't')

    def test_allstrings(self):
        """checks for max when all values are strings."""
        lst = ["string", "height", "hi"]
        self.assertEqual(max_integer(lst), "string")

    def test_empty_string(self):
        """checks for max when empty string is passed."""
        lst = ""
        self.assertEqual(max_integer(lst), None)
