#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if sentence is None:
        first = None
    else:
        first = sentence[0]
    return size, first
