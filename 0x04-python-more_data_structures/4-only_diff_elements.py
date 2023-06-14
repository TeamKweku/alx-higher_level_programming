#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ function that returns a set of all elements
        that are present in only one set

        Args:
            set_1: first set
            set_2: second set

        Returns:
            new_set with values not present in either sets
    """
    new_set = set_1.symmetric_difference(set_2)
    return (new_set)
