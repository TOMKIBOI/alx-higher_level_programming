#!/usr/bin/python3
'''module class Square, defined by size attribute'''


class Square:
    '''A calss Square, defined by the size attribute
    size must be an integer, otherwise raise TypeErro
    if size is less than 0, raise a ValueError'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("The size of x must be an integer")
        elif size < 0:
            raise ValueError("The size of x must be >= 0")
        else:
            self.__size = size

    '''The area of a Square'''
    def area(self):
        return self.__size ** 2
