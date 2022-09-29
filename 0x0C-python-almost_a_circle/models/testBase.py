#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        myList = []
        if list_objs:
            for obj in list_objs:
                myList.append(obj.to_dictionary())
        s = cls.to_json_string(myList)

        with open(str(cls.__name__) + ".json", "w") as f:
            f.write(s)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
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
        text = ""

        # create string from list of objects
        if list_objs:
            filenameRect = cls.__name__ + ".csv"
            filenameSq = cls.__name__ + ".csv"
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    with open(filenameRect, "a") as fRect:
                        text = cls.__name__ + ": "
                        text += str(obj.id) + ","
                        text += str(obj.width) + "," + str(obj.height) + ","
                        text += str(obj.x) + "," + str(obj.y) + "\n"

                        # write to Rectangle.csv file
                        fRect.write(text)
                elif cls.__name__ == "Square":
                    with open(filenameSq, "a") as fSq:
                        text = cls.__name__ + ": "
                        text += str(obj.id) + ","
                        text += str(obj.width) + ","
                        text += str(obj.x) + "," + str(obj.y) + "\n"

                        # write to Square.csv file
                        fSq.write(text)
                # reset text string
                text = ""

    @classmethod
    def load_from_file_csv(cls):
        rectangleAttr = ["id", "width", "height", "x", "y"]
        squareAttr = ["id", "size", "x", "y"]
        filename = cls.__name__ + ".csv"

        myList = []
        text = ""
        with open(filename, "r") as f:
            print("READ FROM FILE: ", filename)
            text = f.readline()
            if len(text) == 0:
                return []

            text = text.strip("Rectangle: ")
            text = text.strip("\n")
            myList = text.split(",")
            print("***myLIST: ", myList)
            d = {}
            r = []
            for k, arg in zip(rectangleAttr, myList):
                print("***k, arg: ", type(k), type(arg), k, arg)
                setattr(d, k, int(arg))
                print("***d:", d)
            #r1 = Rectangle(myList[0], myList[1], myList[2], myList[3], myList[4])
            #print(r1)

"""
    def load_from_file(cls):
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
"""
