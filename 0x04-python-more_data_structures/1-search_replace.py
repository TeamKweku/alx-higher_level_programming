#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ function that replaces all occurences of an element
        in a list

        Args:
            my_list: the provided list for func
            search: the element to replace in list
            replace: new element

        Return:
            return value. new_list
    """
    if not my_list or not search or not replace:
        return
    new_list = [replace if x == search else x for x in my_list]
    return (new_list)
