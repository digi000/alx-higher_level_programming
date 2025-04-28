#!/usr/bin/python3
"""1. Base class"""
class Base:
    """1. Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            type(self).__nb_objects =+ 1
            self.id = type(self).__nb_objects
