#!/usr/bin/python3
"""class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        ar = self.__size * self.__size
        return ar

    def area(self):
        """square area"""
        return self.__size * self.__size

    def __le__(self, other):
        return (self.__size * self.__size < other.__size * other.__size)

    def __le__(self, other):
        return (self.__size * self.__size <= other.__size * other.__size)

    def __eq__(self, other):
        return (self.__size * self.__size == other.__size * other.__size)

    def __ne__(self, other):
        return (self.__size * self.__size != other.__size * other.__size)

    def __gt__(self, other):
        return (self.__size * self.__size > other.__size * other.__size)

    def __ge__(self, other):
        return (self.__size * self.__size >= other.__size * other.__size)
    pass
