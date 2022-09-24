#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size == 0:
        first = None
    else:
        first = sentence[0]
    return size, first
