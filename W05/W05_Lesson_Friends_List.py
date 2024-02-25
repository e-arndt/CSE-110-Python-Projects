# Author: Eric Arndt
# Class: CSE 110 W05 Friends List
# 

import os
import time

run                 = "Y"

while run == "Y" or run == "y":
    new_line            = "\n"
    friend_name         = ""
    stop                = "end"
    friends_list        = []
    

# Set function for clearing terminal screen
    def clrscr():
    # Check if Operating System is Mac and Linux or Windows
        if os.name == 'posix':
            _ = os.system('clear')
        else:
    # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')


    clrscr()
    print("Create a list of friends to print, enter 'end' to stop.")
    print(new_line)
    while friend_name != stop:
            friend_name = (input("Enter a friend's name: "))
            if friend_name != stop:
                friends_list.append(friend_name)
            else:
                print(new_line)
                print("Your friends are:")
                for friend in friends_list:
                    print(friend)
                print(new_line)
                run = (input('Play again? [Y/N]: '))

if (run == "Y" or run == "y"):
    clrscr()
elif (run != "Y" or run != "y"):
    print("Bye...")
    print(new_line)
