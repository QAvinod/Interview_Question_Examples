"""
Python supports both function and operator overloading.
In function overloading, we can use the same name for many Python
functions but with the different number or types of parameters.
With operator overloading, we are able to change the meaning of a
Python operator within the scope of a class.

"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self):
        print(self.x, self.y)


p1 = Point(1, 2)
len(p1)
