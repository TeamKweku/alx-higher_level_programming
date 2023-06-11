#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Function that prints all int in reverse order

    Args:
        my_list: list to be reversed

    Returns:
        The return value. my_list[::-1]
    """
    if my_list is None or my_list == []:
        return
    for x in (my_list := my_list[::-1]):
        print("{:d}".format(x))
