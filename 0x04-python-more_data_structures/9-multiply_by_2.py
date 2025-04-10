#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    df = a_dictionary.copy()
    for key, value in df.items():
        df[key] = value * 2
    return df
