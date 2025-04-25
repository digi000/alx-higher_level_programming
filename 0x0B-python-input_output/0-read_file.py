#!/usr/bin/python3
"""0. Read file"""
def read_file(filename=""):
    """0. Read file"""
    with open(filename) as f:
        print("{}".format(f.read()), end="")
