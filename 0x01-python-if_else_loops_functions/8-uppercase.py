#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        cv = str[i]
        if ord(cv) >= 97 and ord(cv) <= 122:
            cv = chr(ord(cv) - 32)
        if i < len(str) - 1:
            print("{}".format(cv), end="")
        else:
            print("{}".format(cv))
        i += 1

