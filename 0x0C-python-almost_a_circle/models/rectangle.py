#!/usr/bin/python3
"""2. First Rectangle"""
from models.base import Base
class Rectangle(Base):
    """2. First Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__height = value
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """4. Area first"""
        return self.__width * self.__height
    def display(self):
        """5. Display #0"""
        for t in range(self.__y):
            print()
        for i in range(self.__height):
            for nm in range(self.__x):
                print(" ", end="")
            for m in range(self.__width):
                print("#", end="")
            print()
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    def update(self, *args):
        lt = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, lt[i], args[i])
