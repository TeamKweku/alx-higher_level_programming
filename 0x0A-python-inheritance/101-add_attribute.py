#!/usr/bin/python3
"""module to add attribute to object if allowed or raises and error"""


def add_attribute(obj, attr, value):
    """function that tries to add an attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
