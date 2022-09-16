#!/usr/bin/python3
"""
    print_square: prints a square of # characters
"""


def print_square(size):
    """
    prints a square of # characters
    Args:
        size (int): number of columns of # character
    """

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float:
        if size < 0:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * int(size))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
