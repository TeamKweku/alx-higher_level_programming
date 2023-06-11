#!/usr/bin/python3
def no_c(my_string):
    """ Function that removes all chars 'c' or 'C' from
        string

        Args:
            my_string: string to be modified

        Returns:
            the return value. modifed my_string
    """
    if not my_string:
        return ""
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
