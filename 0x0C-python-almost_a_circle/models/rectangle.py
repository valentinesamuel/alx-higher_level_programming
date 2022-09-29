#!/usr/bin/python3
"""
rectangle.py file
"""


from models.base import Base


class Rectangle(Base):
    """
    class Rectangle definition
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ___init__ - initialize Rectangle object
        Vars:
            width(int) - width of Rectangle
            height(int) - height of Rectangle
            x(int) - x position of Rectangle
            y(int) - y position of Rectangle
        Result:
            None
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area - calculates the area of a Rectangle
        Args:
            None
        Return:
            None
        """
        return self.__width * self.__height

    def display(self):
        """
        display - prints the Rectangle to the screen using a character
        Args:
            None
        Return:
            None
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, "#" * self.__width, "\n", end="", sep="")

    def __str__(self):
        """
        __str__ - overload the __str__ method with the format:
[Rectangle] (<id>) <x>/<y> - <width>/<height>
        Args:
            None
        Return:
            None
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id,
            self.x, self.y,
            self.width, self.height)

    def update(self, *args, **kwargs):
        """
        update - update Rectangle instance with variatic attributes
        Args:
            args(unk) - random ordered list of attributes
            kwargs(unk) - random dictionary attributes
        Return:
            None
        """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "width" in kwargs:
                self.width = kwargs.get("width")
            if "height" in kwargs:
                self.height = kwargs.get("height")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """
        to_dictionary - return the dictionary representation of a Rectangle
        Args:
            None
        Return:
            None
        """
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
