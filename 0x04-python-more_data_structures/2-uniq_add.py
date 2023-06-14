#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ function that adds all unique ints in a list

        Args:
            my_list: provided list

        Returns:
            return value. sum of all unique ints in list
    """
    result = 0
    for i in set(my_list):
        result += i
    return (result)
