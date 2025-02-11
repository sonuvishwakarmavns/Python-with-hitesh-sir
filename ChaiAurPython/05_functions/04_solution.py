# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle(radius):
    area=((math.pi)*(radius**2))
    circumference=2*math.pi*radius
    return area ,circumference
    
# print("Area and circumfrance is ",circle(7))

a,c = circle(7)
print("Area :",round(a,2),"\nCircumfrance:",round(c,2))
#quantize(decimal. Decimal('0.00')).
#Decimal(decimal) provides a 50-digit decimal point by default
