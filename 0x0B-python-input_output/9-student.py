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

    def to_json(self):
        """
        function that returns a dict description with simple
        data structures for JSON serialization of an object

        Args:
            obj: object file passed

        Returns:
            JSON serialized attributes of the object
        """
        json_dict = {}
        for attr in dir(self):
            if not attr.startswith("__"):
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[attr] = value

        return json_dict
