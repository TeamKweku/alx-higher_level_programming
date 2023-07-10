#!/usr/bin/python3
""" a module that contains a function that returns all the list of
    all available attributes and methods of an object
"""


def lookup(obj):
    """a function that returns a list of available attributes
        and methods of an object

        Arguments:
            obj(object): a python object

        Return:
            returns a list
    """
    return (dir(obj))
