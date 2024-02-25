# Author: Eric Arndt
# Class: CSE 110 W04 Team_Activity_Part 2
# 
# 

import os
import time
import random

run                 = 'Y'
guesses             = 1
new_line            = '\n'
carriage_return     = '\r'
esc                 = '\x1b'
red_bd              = esc + '[41m'
normal              = esc + '[0m'
welcome_banner      = 'GUESS THE NUMBER'
pick_banner         = 'PICKING A NUMBER...'
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
    global guesses
    guesses = 1
    print(red_bd + pick_banner.center(50,' ') + normal + new_line)
    magic_num = random.randint (1, 100)
    time.sleep(2)
    guess()

     
def guess():
    clrscr()
    global magic_num
    global guesses
    print(red_bd + welcome_banner.center(50,' ') + normal + new_line)
    num_guess = int(input('What is your guess [0-100]? '))

    if (num_guess > magic_num):
            print('Lower')
            guesses = (guesses + 1)
            time.sleep(1)
            guess()
    elif (num_guess < magic_num):
            print('Higher')
            guesses = (guesses + 1)
            time.sleep(1)
            guess()
    elif (num_guess == magic_num):
            print(new_line)
            print(f'You guessed it in {guesses} guesses!')
            time.sleep(2)
            again()
    else:
        print(new_line + "Sorry, I didn't understand that.")
        time.sleep(2)
        guess()


def again():
    print(new_line)
    run = (input('Play again? [Y/N]: '))
    if (run == "Y" or run == "y"):
        start()
    else:
      print(new_line)
      print('Thank you for playing.. Bye')
      print(new_line)


clrscr()
if (run == "Y" or run == "y"):
      start()
else:
        print(new_line)
        print('Thank you for playing.. Bye')
        print(new_line)
