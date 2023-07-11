#!/usr/bin/python3
"""module that implements a class Student"""


class Student:
    """
    a class representation for a student

    Attributes:
        first_name(str): first name of student
        last_name(str): last name of student
        age(int): age of student
    """

    def __init__(self, first_name, last_name, age):
        """method initializes attrs when an instance of the class
        is created
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that returns a dict description with simple
        data structures for JSON serialization of an object

        Args:
            attrs: attributes

        Returns:
            JSON serialized attributes of the object
            """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        replaces all the attributes of the Student instance based
        a dict

        Args:
            json(dict): dict passed
        """
        for attr, value in json.items():
            setattr(self, attr, value)
