# Group 18 W02 Team Project - Areas of Shapes
# math module?
import math

New_Line               = '\n'

# Area of a square
print(New_Line)
square_side    = float(input("What is the length of a side of the square? "))
area_square    = (square_side ** 2)
print(f'The area of the square is: {area_square}')
print(New_Line)

# Area of a rectangle
rec_length     = float(input("What is the length of the rectangle? "))
rec_width      = float(input("What is the width of the rectangle? "))
area_rectangle = (rec_length * rec_width)
print(f'The area of the rectangle is: {area_rectangle}')
print(New_Line)

# Area of a circle
radius         = float(input("What is the radius of the circle? "))
area_circle    = (math.pi) * (radius ** 2)
print(f'The area of the circle is: {area_circle}')
print(New_Line)

