#!/usr/bin/python3
"""class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates rectangle class"""

    def __init__(self, width, height):
        """initializes rectangle"""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def __str__(self):
        """returns string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
