# Author: Eric Arndt
# Class: CSE 110 W07 Lesson Functions P3

import os
import math
import time

New_Line               = '\n'
run = "run"


# Set function for clearing terminal screen
def clrscr():
    # Check if Operating System is Mac and Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')


# Function for area of a square
def compute_area_square(length):
    area_square    = (length ** 2)
    return area_square


# Function for area of a rectangle
def compute_area_rectangle(length, width):
    area_rectangle = (length * width)
    return area_rectangle


# Function for area of a circle
def compute_area_circle(radius):
    area_circle    = (math.pi) * (radius ** 2)
    return area_circle


# while loop until user quits
while run != "n":
    # clear screen
    clrscr()
    # print menu
    print("1 = Square")
    print("2 = Rectangle")
    print("3 = Triangle")
    print("0 = Quit")
    # try this code until error occurs
    try:
        # Request user to select a shape from menu
        user_shape = int(input("What shape do you have? "))
        # If 0 is selected, set run to "n" thereby exiting the while loop and ending the program
        if user_shape == 0:
            print(New_Line)
            print("Bye...")
            print(New_Line)
            run = "n"
            continue
    # execute this code when there is an error
    except ValueError:
            print("Invalid entry.")
            time.sleep(2)
            run = "run"
            continue

    # Square selected, prompt user for entry to find area of square, call function - compute_area_square, print function return
    if user_shape == 1:
        print(New_Line)
        square_side = float(input("What is the length of a side of the square? "))
        square_area = compute_area_square(length = square_side)
        print(f'The area of the square is: {square_area}')
        print(New_Line)
        # Run again?
        rerun = input("Run Again? [Y/N]")
        if rerun.lower() == "y":
            run = "run"
        else:
            print(New_Line)
            print("Bye...")
            print(New_Line)
            run = "n"
    

    # Rectangle selected, prompt user for length and width, call function - compute_area_rectangle, print function return
    elif user_shape == 2:
        print(New_Line)
        rec_length = float(input("What is the length of the rectangle? "))
        rec_width  = float(input("What is the width of the rectangle? "))
        rect_area  = compute_area_rectangle(length = rec_length, width = rec_width)
        print(f'The area of the rectangle is: {rect_area}')
        print(New_Line)
        # Run again?
        rerun = input("Run Again? [Y/N]")
        if rerun.lower() == "y":
            run = "run"
        else:
            print(New_Line)
            print("Bye...")
            print(New_Line)
            run = "n"


    # Circle selected, prompt user for radius, call function - compute_area_circle, print function return
    elif user_shape == 3:
        print(New_Line)
        circle_radius = float(input("What is the radius of the circle? "))
        circle_area   = compute_area_circle(radius = circle_radius)
        print(f'The area of the rectangle is: {circle_area}')
        print(New_Line)
        # Run again?
        rerun = input("Run Again? [Y/N]")
        if rerun.lower() == "y":
            run = "run"
        else:
            print(New_Line)
            print("Bye...")
            print(New_Line)
            run = "n"
    # Else assume an invalid entry
    else:
        print("Invalid entry")
        time.sleep(2)
        run = "run"




