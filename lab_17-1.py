# Author: SCT (AMDG) 4/11/22

from cmath import pi
import math

class Circle: # def class
        """ Circle class represents a circle """
        def get_area(self,radius=3): # def function to calculate are of circle
           """ Calculate area of circle """
           return pi * (radius ** 2) # returns answer from circle formula

# calls functions and printd answer
my_circle = Circle()
print(my_circle.get_area())