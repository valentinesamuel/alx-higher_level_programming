#!/usr/bin/python3
def best_score(my_dict):
    myKey = ""
    max = 0
    if not my_dict:
        return None
    for key in my_dict:
        if my_dict[key] > max:
            max = my_dict[key]
            myKey = key
    return myKey
