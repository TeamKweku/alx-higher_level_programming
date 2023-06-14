#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ function that returns a set of common elements
        in two sets

        Args:
            set_1: first set
            set_2: second set

        Returns:
            return value. intersection of two sets
    """
    new_set = set_1.intersection(set_2)

    return (new_set)
