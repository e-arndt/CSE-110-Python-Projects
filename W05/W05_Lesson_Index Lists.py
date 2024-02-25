# Author: Eric Arndt
# Class: CSE 110 W05 List Index
# 

import os
import time

run                     = "Y"

while run == "Y" or run == "y":
    new_line            = "\n"
    item_name           = ""
    stop                = "quit"
    items_list          = []
    

# Set function for clearing terminal screen
    def clrscr():
    # Check if Operating System is Mac and Linux or Windows
        if os.name == 'posix':
            _ = os.system('clear')
        else:
    # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')


    clrscr()
    print("Create a shopping list of items, enter 'quit' to stop.")
    print(new_line)
    while item_name != stop:
            item_name = (input("Enter an item: "))
            if item_name != stop:
                items_list.append(item_name)
            else:
                print(new_line)
                print("The shopping list is:")
                for item in items_list:
                    print(item)
                print(new_line)
                print("The indexed shopping list is:")
                for item_num in range(len(items_list)):
                    print(f"{item_num}. {items_list[item_num]}")
                print(new_line)
                item_index = int(input("Change which item? "))
                new_item   = (input("What's the new item? "))
                items_list[item_index] = (new_item)
                print(new_line)
                print("The updated shopping list is:")
                for item_num in range(len(items_list)):
                    print(f"{item_num}. {items_list[item_num]}")
                print(new_line)
                run = (input('Play again? [Y/N]: '))

if (run == "Y" or run == "y"):
    clrscr()
elif (run != "Y" or run != "y"):
    print("Bye...")
    print(new_line)
