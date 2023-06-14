#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ function that replaces or adds key/value in
        a dictionary

        Args:
            a_dictionary: provided dictionary
            key: key provided
            value: value to be updated or added

        Returns:
            new updated dictionary
    """
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

    return (a_dictionary)
