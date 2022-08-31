#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newArr = []
    for row in matrix:
        temp = list(map(lambda x: x*x, row))
        newArr.append(temp)
    return (newArr)
