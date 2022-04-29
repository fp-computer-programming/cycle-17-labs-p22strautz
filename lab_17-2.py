# Author: SCT (AMDG) 4/11/22

import math

class Circle: # def class
    def __init__(self): # base circle
        self.radius = 1
    def get_area(self,radius): # def function to calculate are of circle
           """ Calculate area of circle """
           return pi * (radius ** 2) # returns answer from circle formula
    def get_diameter(self): # diameter equation to find diameter
        return self.radius * 2 
    def get_perimeter(self): # circumference equation to find circumference
        return (self.get_diameter() * math.pi)
        # all return answer


my_circle = Circle() # function calls and printing
my_circle.radius = 3
print(my_circle.get_perimeter())