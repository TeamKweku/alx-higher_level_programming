#!/usr/bin/python3
"""a module that check if an object is a subclass of a class"""


def inherits_from(obj, a_class):
    """
    function that checks if an object is an instance of a class that
    that inherited (directly or indirectly) from a specified class

    Arguments:
        obj(object): the object to be checked
        a_class(class): the class to be compared against

    Returns:
        True if an instance of the inherited class or False Otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
