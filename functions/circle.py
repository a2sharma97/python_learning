import math

def area_of_circle(radius):
   area =  math.pi * radius ** 2
   circumference = 2 * math.pi * radius
   return area, circumference


a, c = area_of_circle(5)
print("Area the circle is:",a) 
print("Circumference the circle is:",c) 