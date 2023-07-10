#!/usr/bin/python3
"""A module that defines a class that inherits from the list obj"""


class MyList(list):
    """this is an implementation of a class that inherits from
        the list class.

    """
    def print_sorted(self):
        """method that prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
