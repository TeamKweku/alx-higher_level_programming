#!/usr/bin/python3
"""a module that implements a function that returns dict
    with a simple data structure for JSON serialization of
    an object
"""


def class_to_json(obj):
    """
    function that returns a dict description with simple
    data structures for JSON serialization of an object

    Args:
        obj: object file passed

    Returns:
        JSON serialized attributes of the object
    """
    json_dict = {}
    for attr in dir(obj):
        if not attr.startswith('__'):
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[attr] = value

    return json_dict
