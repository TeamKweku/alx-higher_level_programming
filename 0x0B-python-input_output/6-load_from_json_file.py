#!/usr/bin/python3
"""a module that implements a function to load an Object
    from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a JSON file

    Args:
        filename(json): JSON file provided

    Returns:
        returns a python object
    """
    with open(filename, encoding="utf-8") as a_file:
        obj = json.load(a_file)
        return obj
