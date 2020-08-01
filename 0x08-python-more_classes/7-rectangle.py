#!/usr/bin/python3
"""classes"""


class Rectangle:
    """rectangle"""
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rec area"""
        ar = self.__width * self.__height
        return (ar)

    def perimeter(self):
        """rec per"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            per = 2 * (self.width + self.__height)
            return (per)

    def __str__(self):
        ch = ""
        if self.__height == 0 or self.__width == 0:
            return ch
        for i in range(self.__height - 1):
            ch += str(self.print_symbol) * self.__width + "\n"
        ch += str(self.print_symbol) * self.__width
        return (ch)

    def __repr__(self):
        """repr"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
pass
