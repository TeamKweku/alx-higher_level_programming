#!/usr/bin/python3
"""A module that defines a class that inherits from the list obj"""


class MyList(list):
    """this is an implementation of a class that inherits from
        the list class.

    """
    def print_sorted(self):
        """method that prints a sorted list"""
        lst_copy = list.copy(self)
        list.sort(lst_copy)
        print(lst_copy)
