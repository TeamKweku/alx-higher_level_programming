#!/usr/bin/python3
"""module that implements a function to write an Obj
    to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file using
    a JSON representation

    Args:
        my_obj(object): object passed
        filename: name of file

    Returns:
        creates a file with filename
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
