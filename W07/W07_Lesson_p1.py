# Author: Eric Arndt
# Class: CSE 110 W07 Lesson Functions P1

import os

# Set function for clearing terminal screen
def clrscr():
    # Check if Operating System is Mac and Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')

def display_regular(message):
    print(f"Regular: {message}")


def display_uppercase(message):
    print(f"Upper  : {message.upper()}")


def display_lowercase(message):
    print(f"Lower  : {message.lower()}")


clrscr()
print()
user_message = input("Enter a message: ")
display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)
print()
