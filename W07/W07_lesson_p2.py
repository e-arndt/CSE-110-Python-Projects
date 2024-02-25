# Author: Eric Arndt
# Class: CSE 110 W07 Lesson Functions P2

import os


New_Line               = '\n'

# Set function for clearing terminal screen
def clrscr():
    # Check if Operating System is Mac and Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')


# Area of a square
def compute_area_square(length):
    area_square    = (length ** 2)
    return area_square

clrscr()
print()
square_side = float(input("What is the length of a side of the square? "))
square_area = compute_area_square(length = square_side)
print(f'The area of the square is: {square_area}')
print()
print()





