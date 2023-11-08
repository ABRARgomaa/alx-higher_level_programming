#!/usr/bin/python3
"""module for alx task"""


class BaseGeometry:
    """empty class
    """
    def area(self):
        """for calulation of area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method for BaseGometry class

        Args:
        self
        name
        value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
