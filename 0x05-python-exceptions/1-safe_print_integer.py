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
    except ValueError:
        return False
    else:
        return True
