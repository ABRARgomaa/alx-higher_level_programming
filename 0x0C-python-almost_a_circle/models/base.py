#!/usr/bin/python3
'''module for base class'''


class base:
    '''class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constictor'''
        if id is not None:
            self.id = id
        else:
           base.__nb_objects += 1
           self.id = base.__nb_objects
