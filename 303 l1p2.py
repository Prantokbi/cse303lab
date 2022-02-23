#Write a Python program to find the area and perimeter of a circle. Read inputs from the user.

import math
r=float(input("Enter radius of the circle : "))
print("Area = "+format(math.pi*r**2,'0.2f')+ " perimeter =" + format(2*math.pi*r,'0.2f'))

