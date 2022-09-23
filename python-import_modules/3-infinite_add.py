#!/usr/bin/python3
import sys

sum = 0
n = len(sys.argv)

for i in range(1, n):
    sum = sum + int(sys.argv[i])
print("{}".format(sum))
