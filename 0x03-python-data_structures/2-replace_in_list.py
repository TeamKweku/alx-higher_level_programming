#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ Function that replaces an element in a list

    Args:
        my_list: list to be modified
        idx: index
        element: elem to replace at index

    Returns:
        The return value. my_list[idx] = element
    """
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)
