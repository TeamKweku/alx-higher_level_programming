#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Function that prints all int in reverse order

    Args:
        my_list: list to be reversed

    Returns:
        The return value. my_list[::-1]
    """
    my_list = my_list[::-1]
    for x in my_list:
        print("{:d}".format(x))
