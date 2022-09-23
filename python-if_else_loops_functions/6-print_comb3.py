#!/usr/bin/python3
a = 0
for i in range(10):
    if i == 8:
        print("{}{}".format(i, j))
        break
    for j in range(10):
        if j > a:
            print("{}{}".format(i, j), end=", ")
    a = a + 1
