#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    my_len = 0
    for i in range(0, x):
        try:
            if i >= 0 and i <= 9:
                if my_len < x:
                    print("{:d}".format(my_list[i]), end="")
                    my_len += 1
        except TypeError:
            print("", end="")
        except ValueError:
            print("", end="")
    print()
    return my_len
