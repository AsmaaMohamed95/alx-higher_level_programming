#!/usr/bin/python3
"""
    Integers addition module
"""


def add_integer(a, b=98):
    """
    Adds 2 integers
     Raises:
        TypeError: If a or b is a not an integer and not a float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return result
