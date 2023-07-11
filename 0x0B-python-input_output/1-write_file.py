#!/usr/bin/python3
"""a module that implements a write function that writes a text to
    a file
"""


def write_file(filename="", text=""):
    """
    writes/ overwrites a text to an existing file or creates
    and writes to the file and returns the number of characters

    Args:
        filename(str): name of the file
        text(str): text to be written to the file
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        lines = a_file.write(text)
        return lines
