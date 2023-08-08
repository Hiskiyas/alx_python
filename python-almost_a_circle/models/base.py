#!/usr/bin/python3
"""
This is a class that will be inherited from once the 
base 
"""
class Base:
    """
    This class is the base class for all other classes in the project.
    It manages the id attribute for future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a base object with the id attribute.

        Args:
            id (int, optional): The id value. Defaults to None.

        Attributes:
            id (int): The id value for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
