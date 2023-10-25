#!/usr/bin/python3
"""A module class square"""


class Square:
    """A class square"""

    def __init__(self, size=0):
        """square up
        Args:
            size (int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """uptake value of size
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
        """ find area of a square
        Returns:
            area of square
        """

        return self.__size * self.__size

    def my_print(self):
        """Print a square"""

        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
