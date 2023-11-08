#!/usr/bin/python3
"""module for alx task"""


def inherits_from(obj, a_class):
    """method for alx task

    Args:
    obj
    a_class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
