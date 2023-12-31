#!/usr/bin/python3
"""Define class Square"""


class Square:
    """
    Defines a square
    Args:
        size (int): size of a square
    """
    def __init__(self, size=0):
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
