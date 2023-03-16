#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in my_list:
        counter += 1
    try:
        counter_b = 0
        for i in my_list:
            if counter_b < x:
                counter_b += 1
        print(*my_list[:x], sep="")
        return counter_b
    except:
        print(*my_list[x])
        return counter
