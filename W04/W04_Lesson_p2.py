# Author: Eric Arndt
# Class: CSE 110 W04 Lesson Part 2
# 
# 

import os
import time

new_line           = '\n'
candy              = 'no'

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
        _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

for i in range(3):

    clrscr()
    time.sleep(2)
    candy = (input('May I have a piece of candy? '))

    while (candy == "NO" or candy == "no" or candy == "N" or candy == "n" or candy == "No" or candy == "nO"):
        candy = (input('May I have a piece of candy? '))
    
    print(new_line)
    print('Thanks... Mmm NOM NOM NOM..')
    time.sleep(5)

print(new_line)
print('My tummy hurts... :(')
print(new_line)
print(new_line)
print(new_line)

