#!/usr/bin/python3
"""a module that creates the base model class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method that returns JSON rep of a list_dictionaries

        Args:
            list_dictionaries: list dict of an object
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        method that returns the list of JSON string representation

        Args:
            json_string(str): json string
            
        Returns:
            list of JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that writes JSON string representation of list_objs
        to a file

        Args:
            cls: the class
            list_objs: list object to be written
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        jstr = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write(jstr)
