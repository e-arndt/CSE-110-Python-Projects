# Author: Eric Arndt
# Class: CSE 110 W04 Team_Activity_Part 1
# 
# 

import os
import time

run = 'Y'
new_line            = '\n'
carriage_return     = '\r'
esc                 = '\x1b'
red_bd              = esc + '[41m'
normal              = esc + '[0m'
welcome_banner      = 'GUESS THE NUMBER'
global magic_num

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
        _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

def start():
    clrscr()
    global magic_num
    print(red_bd + welcome_banner.center(50,' ') + normal + new_line)
    magic_num = int(input('What is the MAGIC number [0-100]? '))
    guess()

     
def guess():
    clrscr()
    global magic_num
    print(red_bd + welcome_banner.center(50,' ') + normal + new_line)
    num_guess = int(input('What is your guess [0-100]? '))

    if (num_guess > magic_num):
            print('Lower')
            time.sleep(1)
            guess()
    elif (num_guess < magic_num):
            print('Higher')
            time.sleep(1)
            guess()
    elif (num_guess == magic_num):
            print('You guessed it!')
            time.sleep(2)
            again()
    else:
        print(new_line + "Sorry, I didn't understand that.")
        time.sleep(2)
        guess()


def again():
    run = (input('Play again? [Y/N]: '))
    if (run == "Y" or run == "y"):
        start()
    else:
      print('Thank you for playing.. Bye') 


clrscr()
if (run == "Y" or run == "y"):
      start()
else:
        print('Thank you for playing.. Bye')
        print(new_line)
