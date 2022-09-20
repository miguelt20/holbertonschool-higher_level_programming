#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    positive = number * -1
    lastdigit = positive % 10
    if lastdigit != 0:
        print(f"Last digit of {number}\
 is {-lastdigit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {lastdigit} and is 0")
else:
    lastdigit2 = number % 10
    if lastdigit2 > 5:
        print(f"Last digit of {number} is\
 {lastdigit2} and is greater than 5")
    elif lastdigit2 < 6 and lastdigit2 > 0:
        print(f"Last digit of {number} is\
 {lastdigit2} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {lastdigit2} and is 0")
