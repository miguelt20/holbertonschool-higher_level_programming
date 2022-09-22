#!/usr/bin/python3
def uppercase(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for x in str:
        for pos in range(52):
            if alphabet[pos] == x:
                i = pos
        if x not in alphabet or i>=26:
            result += x
        else:
            result += alphabet[i+26]
    print(result)
