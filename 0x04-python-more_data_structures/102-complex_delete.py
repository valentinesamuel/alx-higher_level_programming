i#!/usr/bin/python3
def complex_delete(my_dict, value):
    a = []
    for key in my_dict:
        if my_dict[key] == value:
            a.append(key)
    for x in a:
        del my_dict[x]
    return my_dict
