#!/usr/bin/python3
"""a module that implements a function that appends a string"""


def append_write(filename="", text=""):
    """
    appends a string at the end of text file(UTF8) and
    returns the number of characters added

    Args:
        filename: name of file
        text: text to be appended
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        lines = a_file.write(text)
        return lines
