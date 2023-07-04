#!/usr/bin/python3
""" a module that prints a name """


def say_my_name(first_name, last_name=""):
    """
    a function that prints a name based on first and last names
    provided

    Args:
        first_name (str): first name
        last_name (str): last name (optional)

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
