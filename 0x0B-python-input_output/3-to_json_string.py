#!/usr/bin/python3
"""a module that returns a JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object as a string

    Args:
        my_obj: object passed
    """
    str_obj = json.dumps(my_obj)
    return str_obj
