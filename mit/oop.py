#!/usr/bin/env python3 

# creating class coordinate

class Coordinate(object):
    """
    Class for 2D coordinates: accept two integers (x, y)
    By default coordinate x = 0 and y = 0.
    """
    def __init__(self, x=0 , y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        x_dist = (other.x - self.x) ** 2
        y_dist = (other.y - self.y) ** 2
        return (x_dist + y_dist) ** 0.5
    
    def __str__(self):
        # print(self)
        return "<<<"+ str(self.x) + ":" +str(self.y) + ">>>"

a = Coordinate(5, 2)
b = Coordinate(11, 7)
print(a)
print(b)

dist = a.distance(b)
print(dist)
# if you want to do somethink with your objects, like add (a + b). 
# Python dont't know haw to add two objects
# in this case you need to implement special methods:
# special methods ready to define are:
"""
__add__(self, other)   --->    self + other
__sub__(self, other)   --->    self - other
__eq__(self, other)    --->    self == other
__lt__(self, other)    --->    self < other
__len__(self)          --->    len(self)
__str__(self)          --->    print self
...
and others
"""
