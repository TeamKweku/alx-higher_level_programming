#!/usr/bin/python3
"""a module that seperates a text per provided punctuations"""


def text_indentation(text):
    """
    function that indents a text based on provided punctuations

    Args:
        text(str): the provided text

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punct = ['.', '?', ':']
    i = 0

    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in punct:
            if text[i] in punct:
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
