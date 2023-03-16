#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    counter, res = 0, 0
    new_list = []
    try:
        for i in range(0, list_length):
            try:
                res = my_list_1[counter] / my_list_2[counter]
            except ZeroDivisionError:
                print("division by 0")
                res = 0
            except TypeError:
                print("wrong type")
                res = 0
            except IndexError:
                print("out of range")
                res = 0
            new_list.append(res)
            counter += 1
    finally:
        return new_list
