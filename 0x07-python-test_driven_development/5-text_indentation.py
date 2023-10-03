#!/usr/bin/python3
"""
Defines a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text: String to be indented
    Raises:
        TypeError: If text is not a string.
    """
    delims = '.?:'
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for txt in text:
        print(txt, end="")
        if txt in delims:
            print("\n\n", end="")
