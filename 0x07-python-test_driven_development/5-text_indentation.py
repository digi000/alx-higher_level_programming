#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ['.','?',':']:
            print("{}".format(text[i]))
            print("")
        else:
            print("{}".format(text[i]), end="")
        i += 1
