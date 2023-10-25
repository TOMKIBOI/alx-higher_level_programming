#!/usr/bin/python3
"""A module class square"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """uptakesquare
        Args:
            size (int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """check for the value of size
        Returns:
            size (int)
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ new value of size
        Args:
            value (int): new value of size
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Find area of a square
        Returns:
            area of the square
        """

        return self.__size * self.__size
