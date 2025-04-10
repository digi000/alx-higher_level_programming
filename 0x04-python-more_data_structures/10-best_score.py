#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mx = 0
    ms = "fg"
    for ky, vl in a_dictionary.items():
        if vl > mx:
            mx = vl
            ms = ky
    return ms

