def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        new_list.append(x if x != search else replace)
    return new_list
