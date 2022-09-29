#!/usr/bin/python3

from models.testBase import Base


class Rectangle(Base):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.__height * self.__width

    def display(self):
        for vertical in range(self.y):
            print()
        for horizontal in range(self.height):
            print(" " * self.__x, "#" * self.__width, "\n", end="", sep="")

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id,
            self.x, self.y,
            self.width, self.height)

    def update(self, *args, **kwargs):
        attrs = ["id", "width", "height", "x", "y"]
        for k, arg in zip(attrs, args):
            setattr(self, k, arg)

        for key, v in kwargs.items():
            setattr(self, key, v)

    def to_dictionary(self):
        result = {}
        attrs = ["id", "width", "height", "x", "y"]
        for i in attrs:
            result[i] = getattr(self, i)
        return result
