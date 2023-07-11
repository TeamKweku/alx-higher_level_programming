#!/usr/bin/python3
"""a module that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    function that returns an object(Python Data structure)
    represented by a JSON string

    Args:
        my_str(json): string to be returned
    """
    json_str = json.loads(my_str)
    return json_str
