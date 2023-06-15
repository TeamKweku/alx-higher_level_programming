#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ function that deletes keys with a specific value
        in a dictionary

        Args:
            a_dictionary: provided dictionary
            value: value to delete related keys

        Returns:
            modified list
    """
    if not value:
        return (a_dictionary)
    keys_to_del = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_del:
        del a_dictionary[key]

    return (a_dictionary)
