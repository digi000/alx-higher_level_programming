#!/usr/bin/python3
"""1. Base class"""
import json
class Base:
    """1. Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
