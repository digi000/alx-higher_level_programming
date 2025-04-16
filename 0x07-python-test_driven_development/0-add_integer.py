#!/usr/bin/python3
"""must be integers or floats, otherwise rais"""
def add_integer(a, b=98):
    """def add_integer(a, b=98):"""
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
