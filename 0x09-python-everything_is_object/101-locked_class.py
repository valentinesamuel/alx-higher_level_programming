#!/usr/bin/python3
class LockedClass:
    """
    LockedClass - has no class or object attribute. It prevents the user
    to dynamically create new instance attributes, except for first_name
    """
    __slots__ = ['first_name']

    def __init__(self, name=""):
        """
        Initialize LockedClass instance
        Args:
            name (str): first name for assignment
        """
        if type(name) is str:
            self.first_name = name
