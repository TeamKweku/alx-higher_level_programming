#!/usr/bin/python3
def best_score(a_dictionary):
    """ function that returns a key with the biggest
        int value.

        Args:
            a_dictionary: provided dictionary

        Returns:
            max value key
    """
    if not a_dictionary:
        return (None)
    max_value = 0
    max_key = None
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return (max_key)
