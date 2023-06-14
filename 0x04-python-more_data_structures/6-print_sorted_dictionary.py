#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ function that prints dict in ordered keys

        Args:
            a_dictionary: dictionary to func

        Returns:
            prints sorted key : value pair
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
