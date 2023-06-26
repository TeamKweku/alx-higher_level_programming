#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an integer with "{:d}".format()

    Args:
        value: value provided to func
    Return:
        True if printed correctly or False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
