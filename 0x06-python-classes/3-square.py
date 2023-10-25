#!/usr/bin/python3
"""Defines the square"""


class Square:
    """The square"""
    def __init__(self, size=0):
        """Initialeze the square.

        Args:
        Size(int):size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Returns the currnt square area"""
            return (self.__size * self.__size)
