#!/usr/bin/python3
def multiple_returns(sentence):
    """ Function that returns a tuple with length of
        string and its first character.
    """
    if len(sentence) == 0:
        str_len, char = 0, None
    else:
        str_len, char = len(sentence), sentence[0]
    str_tuple = str_len, char

    return (str_tuple)
