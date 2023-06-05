class Rectangle:
    def __init__(self, width=0, height=0):
self.__width = width
self.__height = height

    @property
    def width(self):
    return self.__width

    @width.setter
    def width(self, value):
        
