#!/usr/bin/python3
"""1. Write to a file"""
def write_file(filename="", text=""):
    """1. Write to a file"""
    with open(filename, 'w', 'UTF8') as f:
        nc = f.write(text)
        return nc
