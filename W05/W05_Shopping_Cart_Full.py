# Author: Eric Arndt
# Class: CSE 110 W05 Shopping Cart Full
# 

import os
import time
esc                 = '\x1b'
red_bd              = esc + '[41m'
normal              = esc + '[0m'
main_banner         = "SHOPPING CART MENU"
add_banner          = "ADD ITEM TO CART"
cart_banner         = "SHOPPING CART ITEMS"
remove_banner       = "SHOPPING CART ITEM REMOVAL"
total_banner        = "SHOPPING CART TOTAL"
new_line            = "\n"
new_item            = ""
new_price           = 0
remove_num          = 0
cart_total          = 0
quantity            = 0
list_items          = []
list_prices         = []
run                 = "Y"



while run == "Y" or run == "y":
    
# Set function for clearing terminal screen
    def clrscr():
    # Check if Operating System is Mac and Linux
        if os.name == 'posix':
            _ = os.system('clear')
        else:
    # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')

    def menu():
        clrscr()
        print(red_bd + main_banner.center(50,' ') + normal + new_line)
        print("1. Add a new item")
        print("2. Display shopping cart")
        print("3. Remove an item")
        print("4. Compute the total")
        print("5. Quit")
        print(new_line)
        

    menu()
    menu_opt = (input("Select an option: "))
    if menu_opt.isalpha():
        print("A number must be entered, try again.")
        time.sleep(2)
        menu()
    else:
        menu_opt = int(menu_opt)
        if menu_opt == 1:
            clrscr()
            print(red_bd + add_banner.center(50,' ') + normal + new_line)
            new_item = input("Item to add: ")
            list_items.append(new_item)
            new_price = float(input("Item price: $"))
            list_prices.append(new_price)
            print(f"'{new_item}' has been added.")
            time.sleep(1)
            menu()

        elif menu_opt == 2:
            clrscr()
            print(red_bd + cart_banner.center(50,' ') + normal + new_line)
            for item_num in range(len(list_items)):
                    print(f"{item_num + 1}. {list_items[item_num]} - ${list_prices[item_num]:.2f}")
            print(new_line)
            back = input("Press enter for main menu.")
            menu()

        elif menu_opt == 3:
            clrscr()
            print(red_bd + remove_banner.center(50,' ') + normal + new_line)
            for item_num in range(len(list_items)):
                    print(f"{item_num + 1}. {list_items[item_num]} - ${list_prices[item_num]:.2f}")
            print(new_line)
            item_len = (len(list_items))
            remove_num = int(input("Number of item to remove "))
            remove_item = (remove_num - 1)
            if remove_item < 0 or remove_num > item_len:
                print(f"Not a valid item number.")
                time.sleep(2)
                
            else:
                print(f"'{list_items[remove_item]}' has been removed.")
                list_items.pop(remove_item)
                list_prices.pop(remove_item)
                time.sleep(2)
                menu()

        elif menu_opt == 4:
            clrscr()
            print(red_bd + total_banner.center(50,' ') + normal + new_line)
            for item_num in range(len(list_items)):
                    print(f"{item_num + 1}. {list_items[item_num]} - ${list_prices[item_num]:.2f}")
            print(new_line)
            for item_num in range(len(list_prices)):
                cart_total = (cart_total + list_prices[item_num])
            print(f"Total price of shopping cart items: ${cart_total:.2f}")
            print(new_line)
            back = input("Press enter for main menu.")
            cart_total = 0
            menu()

        elif menu_opt == 5:
            print(new_line)
            run = "N"

        else:
            print("Please enter a valid number")
            time.sleep(2)
            run = "Y"

    

if (run == "Y" or run == "y"):
    clrscr()
elif (run != "Y" or run != "y"):
    print("Bye...")
    print(new_line)
