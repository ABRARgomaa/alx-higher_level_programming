#!/usr/bin/python3
"""module for alx task"""


class MyList(list):
    """Mylist child class

    Args:
    list
    """
    def print_sorted(self):
        """method for alx task
        """
        print(sorted(self))
