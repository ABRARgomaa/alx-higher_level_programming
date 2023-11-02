#!/usr/bin/python3
"""Reactangle Module"""


class Rectangle:
    """Creates a Reactangle"""

    def __init__(self, width=0, height=0):
         """Create instances for a rectangle

         Args:
         width and height
         """
         self.height = height
         self.width = width

    @Property
    def width(self):
        return (self.__width)

    @Width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @Property
    def height(self):
        return (self.__height)

    @Height.setter
     def height(self, value):
         if (not isinstance(value, int)):
             raise TypeError("height must be an integer")
         if value < 0:
             raise ValueError("height must be >= 0")
         self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            string += "\n"
        return (string)
