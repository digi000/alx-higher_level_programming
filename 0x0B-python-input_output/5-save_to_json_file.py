#!/usr/bin/python3
"""5. Save Object to a file"""
import json
def save_to_json_file(my_obj, filename):
    """def save_to_json_file(my_obj, filename):"""
    with open(filename, 'w' encoding="UTF8") as f:
        json.dump(my_obj, f)
