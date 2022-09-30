#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in my_list:
        try:
            if i >= 0 and i <= 9:
                if counter < x:
                    print("{:d}".format(i), end="")
                    counter += 1
        except:
            print("", end="")
    print()
    return counter
