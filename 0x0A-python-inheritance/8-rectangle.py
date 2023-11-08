#!/usr/bin/python3
"""module for alx task"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class for alx task
    """
    def __init__(self, width, height):
        """init method for height and width

        Args:
        width
        height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
