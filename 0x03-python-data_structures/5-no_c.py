#!/usr/bin/python3
def no_c(my_string):
    nl = list(my_string)
    ln = len(nl) - 1
    for i in range(ln, -1, -1):
        if nl[i] == "c" or nl[i] == "C":
            del nl[i]
            ln -= 1
    st = "".join(nl)
    return st
