#!/usr/bin/python3
"""
This function inherits the basic properties of a polygon from the
rectangle class to the square class.
"""


class BaseGeometry:
    """
    This class represents a base geometry.
    """

    def area(self):
        """
        Calculates the area.

        Raises:
            Exception: with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the integer value.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle object with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns the rectangle description.

        Returns:
            str: The rectangle description in the format "[Rectangle]
            <width>/<height>"
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    This class represents a square.
    """

    def __init__(self, size):
        """
        Initializes a square object with size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
