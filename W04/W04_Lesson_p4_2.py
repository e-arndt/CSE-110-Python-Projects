# Author: Eric Arndt
# Class: CSE 110 W04 Lesson Part 4
# A letter by specific position
# 

import os
import time

new_line           = '\n'
word = "Commitment"

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
        _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

clrscr()
print(new_line)
fav_letter = input('My favorite letter is? ')

for letter in word:
    if letter.lower() == fav_letter.lower():
        print(letter.upper(),end='')
    else:
        print(letter.lower(),end='')
        
print(new_line)
