# Author: Eric Arndt
# Class: CSE 110 W04 Lesson Part 1
# 
# 

import os

new_line            = '\n'
number              = 0

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
        _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')


clrscr()
number = int(input('Enter a positve number: '))

while number <0:
    print('Sorry, not a positive number. Please try again.')
    number = int(input('Enter a positve number: '))
    

print(f'The number is: {number}')
