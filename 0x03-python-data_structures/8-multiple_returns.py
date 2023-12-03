#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        x = len(sentence)
        f = sentence[0]
        return (x, f)
