#!/usr/bin/python3
"""module for alx task"""


def is_kind_of_class(obj, a_class):
    """method for alx task

    Args:
    obj
    a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
