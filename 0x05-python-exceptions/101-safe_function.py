#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    function that executes a function safely

    Args:
        fct: function to be executed
        args: the arguments to function

    Return:
        result of function
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
