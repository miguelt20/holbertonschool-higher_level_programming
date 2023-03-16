#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except:
        print("Inside result: None")
        return None
    finally:
        try:
            print("Inside result: {}".format(a/b))
        except:
            return None
