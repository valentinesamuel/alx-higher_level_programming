#!/usr/bin/python3
"""
    say_my_name: function that prints "My name is "
"""


def say_my_name(first_name, last_name=""):
    """ Print 'My name is first_name last_name'
    first_name and last_name must be strings
    Args:
    first_name (str): first name of person
    last_name (str): last name of person
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
