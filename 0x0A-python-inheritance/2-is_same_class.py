#!/usr/bin/python3
"""Module that Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The tch the type of obj to.
    Returns:
        If obj is exactly ace of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
