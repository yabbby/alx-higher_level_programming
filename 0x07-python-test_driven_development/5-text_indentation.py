#!/usr/bin/python3
"""
    Module with function on text indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines when character [., ?, :] appear

    :param text: str

    :return None

    :raises TypeError: when text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    at_beg_line = True
    for char in text:
        if at_beg_line and char == " ":
            continue
        if char in [".", "?", ":"]:
            print("{}\n".format(char))
            at_beg_line = True
        else:
            print(char, end="")
            at_beg_line = False
