# Author: Eric Arndt
# Class: CSE 110 W05 Shopping Cart Milestone
# 
# import libraries, set variables and lists
import os
import time
esc                 = '\x1b'
red_bd              = esc + '[41m'
normal              = esc + '[0m'
cart_banner         = "SHOPPING CART FUNCTIONS"
new_line            = "\n"
new_item            = ""
list_items          = []
list_prices         = []
run                 = "Y"


# Loop unti user quits
while run == "Y" or run == "y":
    
# Set function for clearing terminal screen
    def clrscr():
    # Check if Operating System is Mac and Linux
        if os.name == 'posix':
            _ = os.system('clear')
        else:
    # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')

# Setup menu function
    def menu():
        clrscr()
        print(red_bd + cart_banner.center(50,' ') + normal + new_line)
        print("1. Add a new item")
        print("2. Display shopping cart")
        print("3. Remove an item")
        print("4. Compute the total")
        print("5. Quit")
        print(new_line)
        
# Call menu function, request user input for menu options
    menu()
    menu_opt = (input("Select an option: "))
    # Handle input that is not a number
    if menu_opt.isalpha():
        print("A number must be entered, try again.")
        time.sleep(2)
        menu()
    else:
        # Convert user input to an integer
        menu_opt = int(menu_opt)
        # If input option 1 selected, request user to enter item name to add to cart
        if menu_opt == 1:
            print(new_line)
            new_item = input("Item to add: ")
            # Append item entered to item list
            list_items.append(new_item)
            print(f"'{new_item}' has been added to the cart.")
            time.sleep(1)
            menu()

        # If option 2, display items in shopping cart
        elif menu_opt == 2:
            print(new_line)
            print("Items in shopping cart:")
            # If item list is empty, tell user the cart is currently empty
            if (len(list_items) == 0):
                print("Cart is empty")
            # Otherwise recall item names from item list and print contents to user
            else:
                for item_num in range(len(list_items)):
                    print(f"{item_num + 1}. {list_items[item_num]}")
            print(new_line)
            back = input("Press enter to continue.")
            menu()

        # Option 3 will allow user to remove items from the item list
        elif menu_opt == 3:
            print(new_line)
            print("Remove item function here.")
            time.sleep(2)

        # Option 4 will display the total price of all items
        elif menu_opt == 4:
            print(new_line)
            print("Compute total function here.")
            time.sleep(2)

        # Option 5 allows the user to quit the program
        elif menu_opt == 5:
            print(new_line)
            run = "N"

        else:
            print("Please enter a valid number")
            time.sleep(2)
            run = "Y"

    
# Continues or discontinues the while loop
if (run == "Y" or run == "y"):
    clrscr()
elif (run != "Y" or run != "y"):
    print("Bye...")
    print(new_line)
