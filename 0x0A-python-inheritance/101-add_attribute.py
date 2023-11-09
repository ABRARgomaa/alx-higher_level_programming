#!/usr/bin/python3
"""module for alx tasks"""


def add_attribute(obj, att, value):
    """alx task method
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
