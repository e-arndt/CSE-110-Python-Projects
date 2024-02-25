# Author: Eric Arndt
# Class: CSE 110 W03 Adventure Game
# 
# 

import os
import time


new_line            = '\n'
esc                 = '\x1b'
red_bd              = esc + '[41m'
normal              = esc + '[0m'
welcome_banner      = 'WELCOME TO TEXT ADVENTURE 1'
living_room_banner  = 'LIVING ROOM'
instruction_banner  = 'INSTRUCTIONS'
kitchen_banner      = 'KITCHEN'
bathroom_banner     = 'BATHROOM'


def instruct():
    clrscr()
    print(red_bd + instruction_banner.center(50,' ') + normal + new_line)
    print('Use the words in all CAPS to perform actions.')
    print('The first letter of any all CAPS word can also be used.')
    print('Exapmle r for RUN or d for DOOR.')
    print('Both Upper or Lower case will work.')
    print('Press "Enter" after each word or letter.')
    print(new_line)
    input('Press "Enter" key when ready to continue: ')
    living_room()

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
        _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')


def huh():
    print(new_line + "Sorry, I didn't understand that.")
    time.sleep(2)


def kitchen():
    clrscr()
    print(red_bd + kitchen_banner.center(50,' ') + normal + new_line)
    print('You see a SINK, stove, REFRIGERATOR and the LIVING room.')
    action    = input('Enter your choice: ')
    if (action == "SINK" or action == "sink" or action == "S" or action == "s"):
        print(new_line + 'You get a glass a water and drink it... Ahhhh...')
        time.sleep(3)
        kitchen()
    elif (action == "REFRIGERATOR" or action == "refrigerator" or action == "R" or action == "r"):
        print(new_line + 'You make yourself a sandwich and eat it, Mmmm...')
        time.sleep(4)
        kitchen()
    elif (action == "LIVING" or action == "living" or action == "L" or action == "l"):
        print(new_line + 'You walk into the Living Room.')
        time.sleep(3)
        living_room()
    else:
        huh()
        kitchen()

def bathroom():
    clrscr()
    print(red_bd + bathroom_banner.center(50,' ') + normal + new_line)
    print('You see a SINK, a TOILET and the LIVING Room door.')
    action    = input('Enter your choice: ')
    if (action == "SINK" or action == "sink" or action == "S" or action == "s"):
        print(new_line + 'You wash your hands.')
        time.sleep(4)
        bathroom()
    elif (action == "TOILET" or action == "toilet" or action == "T" or action == "t"):
        print(new_line + 'You use the toilet, better wash your hands.')
        time.sleep(4)
        bathroom()
    elif (action == "LIVING" or action == "living" or action == "L" or action == "l"):
        print(new_line + 'You walk back into the Living Room.')
        time.sleep(4)
        living_room()
    else:
        huh()
        bathroom()

def living_room():
    clrscr()
    print(red_bd + living_room_banner.center(50,' ') + normal + new_line)
    print('You see a COUCH, TV, KITCHEN and a BATHROOM door.')
    action    = input('Enter your choice: ')
    if (action == "COUCH" or action == "couch" or action == "C" or action == "c"):
        print(new_line + 'You sit on the couch and watch TV.')
        time.sleep(5)
        living_room()
    elif (action == "TV" or action == "tv" or action == "T" or action == "t"):
        print(new_line + 'You notice the TV is on.')
        time.sleep(2)
        living_room()
    elif (action == "KITCHEN" or action == "KITCHEN" or action == "K" or action == "k"):
        print(new_line + 'You walk into the Kitchen.')
        time.sleep(3)
        kitchen()
    elif (action == "BATHROOM" or action == "bathroom" or action == "B" or action == "b"):
        print(new_line + 'You walk into the Bathroom.')
        time.sleep(3)
        bathroom()
    else:
        huh()
        living_room()


clrscr()
print(red_bd + welcome_banner.center(50,' ') + normal + new_line)
instructions = input('Do you want instructions [Y/N]? ')

if (instructions == "Y" or instructions == "y"):
    instruct()
elif (instructions == "N" or instructions == "n"):
    living_room()
else:
    print('Thank you for playing, bye.')
    


