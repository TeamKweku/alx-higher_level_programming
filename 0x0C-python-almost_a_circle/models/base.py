#!/usr/bin/python3
"""a module that creates the base model class """


class Base:
    """
    This is an implementation of a rectangle class

    Attributes:
        nb_objects: private class attribute

        id(int): id of the instance of the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
