# Author: Eric Arndt
# Class: CSE 110 W05 Team_Activity_Part 1
# 

import os
import time

run                 = 'Y'

while run == "Y" or run == "y":
    new_line            = '\n'
    user_num            = 1
    end_num             = 0

    num_list            = []

# Set function for clearing terminal screen
    def clrscr():
    # Check if Operating System is Mac and Linux or Windows
        if os.name == 'posix':
            _ = os.system('clear')
        else:
    # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')

    
    clrscr()
    print('Enter a list of numbers, enter zero(0) to end.')
    print(new_line)
    while user_num != end_num:
            user_num = int(input("Enter a number: "))
            if user_num == end_num:
                 continue
            num_list.append(user_num)

    else:
        total   = sum(num_list)
        average = total/len(num_list)
        max_num = max(num_list)
        print(new_line)
        print(f"Sum of Numbers: {total}")
        print(f"Average of Sum: {average}")
        print(f"Largest Number: {max_num}")
        print(new_line)
        run = (input('Play again? [Y/N]: '))

if (run == "Y" or run == "y"):
    clrscr()
elif (run != "Y" or run != "y"):
    print("Bye...")
    print(new_line)
