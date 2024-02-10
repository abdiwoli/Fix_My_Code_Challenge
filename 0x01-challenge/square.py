#!/usr/bin/python3
""" Module for square class"""


class Square():
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Init method """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ The area """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter insead of root """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ str class """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ init the object object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
