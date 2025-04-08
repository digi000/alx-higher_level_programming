#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    bn = dir(hidden_4)
    for i in range(0, len(bn)):
        cv = bn[i]
        if cv[i] != "_":
            print("{}".format(cv))
