#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dk = sorted(a_dictionary)
    for i in range(len(a_dictionary)):
        print("{}: {}".format(dk[i], a_dictionary[dk[i]]))
