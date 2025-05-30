#!/usr/bin/python3
"""class Square that defines a square"""
class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """size must be >= 0"""
        self.size = size
    def area(self):
        """ returns the current square area"""
        return self.__size * self.__size
    @property
    def size(self):
        """at returns the current square area"""
        return self.__size
    @size.setter
    def size(self, size):
        """at returns the current square area"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__size):
                    print("#", end="")
                print()
