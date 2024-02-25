# Author: Eric Arndt
# Class: CSE 110 W01 Assignment 2
# Request name input, display last name, first name and last name

# Request first and last name from user
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
# drop a line / carriage return
print()
# Set the variable "output" to equal the the user entered data formatted as last name, first last with names capitalized
output = f'Your name is {last_name.capitalize()}, {first_name.capitalize()} {last_name.capitalize()}.'
# Display the variable "output"
print(output)
