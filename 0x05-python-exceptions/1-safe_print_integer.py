#!/usr/bin/python3
def safe_print_integer(value):
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
    except (ValueError, TypeError):
        return False
