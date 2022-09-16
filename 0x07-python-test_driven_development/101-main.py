#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
# test no args
# print(lazy_matrix_mul())
# test one too few args
# print(lazy_matrix_mul([[1, 2], [3, 4]]))
# test too many args
# print(lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]))
# test normal with ints and floats
print(lazy_matrix_mul([[1, 2], [3, 4]], [[1.5, 2.5, 3.5], [4.5, 6.5, 7.5]]))
