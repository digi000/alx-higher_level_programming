#!/usr/bin/python3
def print_last_digit(number):
    cv = None
    if number < 0:
        cv = number % -10
        cv = cv * -1
    else:
        cv = number % 10
    print("{}".format(cv), end="")
    return cv
