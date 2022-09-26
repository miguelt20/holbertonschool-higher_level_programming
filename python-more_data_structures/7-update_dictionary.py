#1/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_element = {key: value}
    a_dictionary.update(new_element)
    return a_dictionary
