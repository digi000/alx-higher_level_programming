#!/usr/bin/python3
"""class Square that defines a square"""
class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """size must be >= 0"""
        self.size = size
        self.position = position
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
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for h in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
