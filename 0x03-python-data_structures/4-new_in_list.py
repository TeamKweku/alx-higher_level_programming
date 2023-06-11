#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ function that replaces an element in a cpy of
    a list

    Args:
        my_list: list provided
        idx: index of element
        element: element to replace original

    Returns:
        The return value. new_list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return (new_list := my_list[:])
    new_list = my_list[:]
    new_list[idx] = element

    return (new_list)
