#!/usr/bin/python3
"""module for alx task"""


def is_same_class(obj, a_class):
    """is_same_class method

    Args:
    obj
    a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
