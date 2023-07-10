#!/usr/bin/python3
"""A module that compares an instance of a class"""


def is_same_class(obj, a_class):
    """a function that compares two classes to confirm if
    they both instance of the same class

    Arguments:
        obj: object to be passed to function
        a_class: a class to be compared with

    Return:
        True is instance or False otherwise
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
