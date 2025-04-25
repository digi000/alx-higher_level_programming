#!/usr/bin/python3
"""6. Create object from a JSON file"""
import json
def load_from_json_file(filename):
    """6. Create object from a JSON file"""
    with open(filename, encoding="UTF8") as f:
        json.load(f)
