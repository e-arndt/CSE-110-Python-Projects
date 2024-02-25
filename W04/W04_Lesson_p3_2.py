# Author: Eric Arndt
# Class: CSE 110 W04 Lesson Part 3
# 
# 

import os
import time

new_line           = '\n'
# colors             = ["red", "blue", "green", "yellow"]

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
        _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

      
print(new_line)
for i in range(2,22,2):
    print(f'The # is: {i}')

print(new_line)
