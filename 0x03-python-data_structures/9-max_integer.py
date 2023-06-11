#!/usr/bin/python3
def max_integer(my_list=[]):
    """ function that finds the biggest int
        in a list

        Args:
            my_list: a list of integers

        Returns:
            the largest int max
    """
    if not my_list or my_list == []:
        return (None)
    max = 0
    for i in my_list:
        if i > max:
            max = i
        else:
            continue
    return (max)
