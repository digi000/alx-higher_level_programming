#!/usr/usr/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp = [0,0,0,0]
    i = 0
    for nt in tuple_a:
        tp[i] = nt
        i += 1
    p = 2
    for nj in tuple_b:
        tp[p] = nj
        p += 1
    return (tp[0] + tp[2], tp[1] + tp[3])
