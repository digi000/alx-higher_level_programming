#!/usr/bin/python3
for i in range(0,10):
    for n in range(1, 10):
        if i == n or n < i:
            continue
        if i != 8 and n != 9:
            print("{}{}, ".format(i, n), end="")
        elif i == 8 and n == 9:
            print("{}{}".format(i, n))
        else:
            print("{}{}, ".format(i, n), end="")
