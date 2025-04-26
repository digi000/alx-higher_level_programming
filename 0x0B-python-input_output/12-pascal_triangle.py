#!/usr/bin/python3
"""Pascal's Triangle"""
def pascal_triangle(n):
    """Pascal's Triangle"""
    if n <= 0:
        return []
    mainlist = []
    duplist1 = [0,1,0]
    duplist2 = []
    main2 = []
    use = []
    free = []

    for i in range(n):
        if i == 0:
            mainlist.append([1])
        else:
            lent = i + 1
            if len(duplist1) == 0:
                free = duplist1
                free.append(0)
                use = duplist2
            else:
                free = duplist2
                free.append(0)
                use = duplist1
            for m in range(lent):
                sumr = use[m] + use[m + 1]
                main2.append(sumr)
                free.append(sumr)
            use.clear()
            mainlist.append(main2.copy())
            main2.clear()
            free.append(0)
    return mainlist
