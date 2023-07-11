#!/usr/bin/python3
"""A module that implements a function to read a text file"""


def read_file(filename=""):
    """
    reads text file and prints it to stdout

    Args:
        filename(str): string rep of the text file
    """
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end="")
