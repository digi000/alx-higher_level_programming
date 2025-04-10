#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) or roman_string == None:
        rv = {'I': 1, 'V': 5,'X': 10, 'L': 50, 'C': 100,'D': 500,'M': 1000}
        rs = roman_string
        sumk = 0
        lf = len(rs)
        i = 0
        while i < lf:
            if lf > i + 1 and rv[rs[i]] < rv[rs[i + 1]]:
                    sumk += rv[rs[i + 1]] - rv[rs[i]]
                    i += 2
                    continue
            sumk += rv[rs[i]]
            i += 1
        return sumk
    return 0
