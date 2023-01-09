#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of the available attributes and methods of an object.

    Parameters:
        obj (object): The object to inspect.

    Returns:
        list: A list of the names of the available attributes and methods of the object.
    """
    return dir(obj)
