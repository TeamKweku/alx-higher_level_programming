#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ function that deletes a key in a dictionary

        Args:
            a_dictionary: provided dictionary
            key: key to be deleted

        Returns:
            updated list with deleted key
    """
    if not key or key not in a_dictionary:
        return (a_dictionary)
    del (a_dictionary[key])
    return (a_dictionary)
