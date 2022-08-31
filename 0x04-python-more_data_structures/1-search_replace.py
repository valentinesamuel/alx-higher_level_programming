#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx in range(0, len(my_list)):
        if my_list[idx] == search:
            my_list[idx] = replace
    return my_list
