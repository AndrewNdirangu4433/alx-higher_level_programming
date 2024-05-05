#!/usr/bin/python3
"""
A class called Rectangle.
"""
class Rectangle:
    """
    this is a class for objects in class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def height(self):
        return self.__height

    def height(self, height):
        """
        This is an attribute for object in class: Rectangle
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height

    def width(self):
        return self.__width

    def width(self, width):
        """
        this is an attribute for a Rectangle object:
        defining its width.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if isinstance(width, int):
            if width < 0:
                raise ValueError("widht must be >= 0")
            self__width = width
 
