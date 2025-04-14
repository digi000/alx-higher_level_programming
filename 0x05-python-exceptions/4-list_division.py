def list_division(my_list_1, my_list_2, list_length):
    mn = len(my_list_1)
    if mn < len(my_list_2):
        mn = len(my_list_2)
    rt = 0
    nl = []
    for i in range(mn):
        try:
            rt = my_list_1[i] / my_list_2[i]
        except TypeError:
            rt = 0
            print("wrong type")
        except ZeroDivisionError:
            rt = 0
            print("division by 0")
        except IndexError:
            rt = 0
            print("out of range")
        finally:
            nl.append(rt)
    return nl
