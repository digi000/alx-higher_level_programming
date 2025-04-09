#!/usr/bin/python3
def multiple_returns(sentence):
    cv = None
    if sentence != "":
        cv = sentence[0]
    return (len(sentence), cv)
