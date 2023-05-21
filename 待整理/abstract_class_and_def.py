# -*- coding: utf-8 -*-
"""
Created on Wed May  3 22:18:26 2023

@author: s9571
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width * self.height
    
circle = Circle(5)
print(circle.getArea())

rectangle = Rectangle(4, 6)
print(rectangle.getArea())