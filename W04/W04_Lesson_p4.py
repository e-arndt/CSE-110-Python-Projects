# Author: Eric Arndt
# Class: CSE 110 W04 Lesson Part 4
# Each letter in a row
# 

import os
import time

new_line           = '\n'
first_name = "Brigham"

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
        _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

clrscr()
print(new_line)

for it in first_name:
    print(f'The letter is: {it}')
print(new_line)
