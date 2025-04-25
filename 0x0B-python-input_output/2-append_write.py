#!/usr/bin/python3
"""2. Append to a file"""
def append_write(filename="", text=""):
    """2. Append to a file"""
    with open(filename, 'a', encoding="UTF8") as f:
        vb = f.write(text)
        return vb
