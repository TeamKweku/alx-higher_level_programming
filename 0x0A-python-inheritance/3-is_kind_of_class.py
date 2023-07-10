#!/usr/bin/python3
"""a module that compares an oject """


def is_kind_of_class(obj, a_class):
    """
    a function that compares two objects to test if the objects
    are instance of or child of a superclass

    Arguments:
        obj: provided object
        a_class: class object to be compared with

    Return:
        True is its an instance or False otherwise
    """
    if not isinstance(obj, a_class):
        return False

    return True
