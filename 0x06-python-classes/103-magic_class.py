#!/usr/bin/python3
"""model MagicClass."""

import math


class MagicClass:
    """Class magiccircle."""

    def __init__(self, radius=0):
        """uptake a MagicClass.
        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
