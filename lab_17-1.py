# Author: SCT (AMDG) 4/11/22

from cmath import pi
import math




class Circle:
        """ Circle class represents a circle """
        def get_area(self):
           """ Calculate area of circle """
           return self.radius
my_circle = Circle()
print(my_circle.get_area())