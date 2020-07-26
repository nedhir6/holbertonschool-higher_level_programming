#!/usr/bin/python3
"""class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """size"""
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
    pass
