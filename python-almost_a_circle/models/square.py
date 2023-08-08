#!/usr/bin/python3
"""
This is a square classs that inherits methods and variables
from the rectangle class.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    This class represents a square and inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square object with size, position, and id.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the square's position. Defaults to 0.
            id (int, optional): The id value. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
