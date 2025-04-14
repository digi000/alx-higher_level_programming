#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cv = 0
        for i in my_list:
            print("{}".format(i), end="")
            cv += 1
            if cv == x:
                break
        print()
    except:
        pass
    return cv
