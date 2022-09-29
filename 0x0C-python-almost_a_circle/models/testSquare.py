#!/usr/bin/python3

from models.testRectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = self.width = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width)

    def update(self, *args, **kwargs):
        attr = ["id", "size", "x", "y"]
        for key, arg in zip(attr, args):
            setattr(self, key, arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        result = {}
        attrs = {"id", "width", "x", "y"}
        for i in attrs:
            if i == "width":
                result["size"] = getattr(self, i)
            else:
                result[i] = getattr(self, i)
        return result
Footer
