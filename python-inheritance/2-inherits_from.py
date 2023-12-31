#!/usr/bin/python3
"""
 This function returns True if the object
 is an instance of a class that inherited
 (directly or indirectly) from the
 specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: Any object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class;
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
