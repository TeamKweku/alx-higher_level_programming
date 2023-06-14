#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ function that returns a new dictionary with
        with all values multiplied by 2

        Args:
            a_dictionary: provided dictionary

        Returns:
            new dictionary with updated values
    """
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return (new_dict)
