#!/usr/bin/python3
"""8. Class to JSON"""
import json
def class_to_json(obj):
    """8. Class to JSON"""
    data = vars(obj)
    return json.dumps(dict(data))
