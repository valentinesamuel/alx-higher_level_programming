#!/usr/bin/python3
""" base.py """


import json
import turtle


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string of a list of dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to file """
        myList = []
        if list_objs:
            for obj in list_objs:
                myList.append(obj.to_dictionary())
        s = cls.to_json_string(myList)

        with open(str(cls.__name__) + ".json", "w") as f:
            f.write(s)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns object instance with values set from **dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Load JSON data from file """
        filename = cls.__name__ + ".json"
        result = test = []
        with open(filename, "r") as f:
            text = f.read()
            if len(text) == 0:
                return []

            myList = []
            result = cls.from_json_string(text)
            for dictionary in result:
                obj = cls.create(**dictionary)
                myList.append(obj)
        return myList

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes a list of Rectangles or Squares in csv to file """
        text = ""

        # create string from list of objects
        if list_objs:
            filenameRect = cls.__name__ + ".csv"
            filenameSq = cls.__name__ + ".csv"
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    with open(filenameRect, "a") as fRect:
                        text += str(obj.id) + ","
                        text += str(obj.width) + "," + str(obj.height) + ","
                        text += str(obj.x) + "," + str(obj.y) + "\n"

                        # write to Rectangle.csv file
                        fRect.write(text)
                elif cls.__name__ == "Square":
                    with open(filenameSq, "a") as fSq:
                        text += str(obj.id) + ","
                        text += str(obj.width) + ","
                        text += str(obj.x) + "," + str(obj.y) + "\n"

                        # write to Square.csv file
                        fSq.write(text)
                # reset text string
                text = ""

    @classmethod
    def load_from_file_csv(cls):
        """ Reads CSV file and deserializes list of Rect / Squares"""
        rectangleAttr = ["id", "width", "height", "x", "y"]
        squareAttr = ["id", "size", "x", "y"]
        filename = cls.__name__ + ".csv"

        myList = []
        r = []
        text = ""
        if filename == "Rectangle.csv":
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip("\n")
                    myList = line.split(",")
                    d = {}

                    for k, arg in zip(rectangleAttr, myList):
                        d[k] = int(arg)

                    obj = cls.create(**d)
                    r.append(obj)
                return r
        elif filename == "Square.csv":
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip("\n")
                    myList = line.split(",")

                    d = {}
                    for k, arg in zip(squareAttr, myList):
                        d[k] = int(arg)
                    obj = cls.create(**d)
                    r.append(obj)
                return r

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Uses Turtle Graphics to draw Rects / Squares """
        pass
