#!/usr/bin/python3
"""class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """size"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @property
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area"""
        ar = self.__size * self.__size
        return ar
    pass
