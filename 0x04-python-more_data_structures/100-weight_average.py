#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0
    result = 0.0
    for j, k in my_list:
        numerator += j * k
        denominator += k
    result = numerator / denominator
    return(result)
