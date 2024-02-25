# CREATIVITY: Drinks and desserts were added. Ability to choose number of items individually added.
# Itemized subtotal added before the full subtotal.
# Red Welcome and Enjoy Meal "banners" were added to dress-up the input / output.


# Author: Eric Arndt
# Class: CSE 110 W02 Meal Price Calculator
# Request prices, quantity, tax and payment inputs, calculate subtotals, tax, total and change due.
# Display calculated data to user.

# Set static variables
new_line            = '\n'
esc                 = '\x1b'
red_bg              = esc + '[41m'
normal              = esc + '[0m'
welcome_banner      = "WELCOME TO BUFFY'S BUFFET "
enjoy_banner        = "ENJOY YOUR MEAL "


# Print "Welcome" Banner
print(red_bg + welcome_banner.center(50,' ') + normal + new_line)
 
# Request input from user for food prices, number of child items, number of adult items and tax rate.
child_meal_price    = float(input("What is the price of a child's meal?     $"))
child_drink_price   = float(input("What is the price of a child's drink?    $"))
child_dessert_price = float(input("What is the price of a child's dessert?  $"))
adult_meal_price    = float(input("What is the price of an adult's meal?    $"))
adult_drink_price   = float(input("What is the price of an adult's drink?   $"))
adult_dessert_price = float(input("What is the price of an adult's dessert? $"))
num_child_meal      = int(input("How many child meals?     "))
num_child_drink     = int(input("How many child drinks?    "))
num_child_dessert   = int(input("How many child desserts?  "))
num_adult_meal      = int(input("How many adults meals?    "))
num_adult_drink     = int(input("How many adults drinks?   "))
num_adult_dessert   = int(input("How many adults desserts? "))
sales_tax_rate      = float(input('Current sales tax rate?   '))


# Claculate Subtotals,Tax and Total.
child_meal_sub      = (child_meal_price * num_child_meal)
child_drink_sub     = (child_drink_price * num_child_drink)
child_dessert_sub   = (child_dessert_price * num_child_dessert)
adult_meal_sub      = (adult_meal_price * num_adult_meal)
adult_drink_sub     = (adult_drink_price * num_adult_drink)
adult_dessert_sub   = (adult_dessert_price * num_adult_dessert)
sub_total           = (child_meal_sub + child_drink_sub + child_dessert_sub) + (adult_meal_sub + adult_drink_sub + adult_dessert_sub)
sales_tax           = sub_total * (sales_tax_rate / 100)
total               = sub_total + sales_tax


# Set variables for displaying itemized subtotals, tax and total calculations.
sub_child_meal      = (f'Child Meals:     ${child_meal_sub:.2f}')
sub_child_drink     = (f'Child Drinks:     ${child_drink_sub:.2f}')
sub_child_dessert   = (f'Child Desserts:   ${child_dessert_sub:.2f}')
sub_adult_meal      = (f'Adult Meals:     ${adult_meal_sub:.2f}')
sub_adult_drink     = (f'Adult Drinks:     ${adult_drink_sub:.2f}')
sub_adult_dessert   = (f'Adult Desserts:  ${adult_dessert_sub:.2f}')
sub_t               = (f'Subtotal:   ${sub_total:.2f}')
s_tax               = (f'Sales Tax:   ${sales_tax:.2f}')
tot                 = (f'Total:      ${total:.2f}')


# Print subtotals, tax and total costs to the user in an easy to read format.
print(new_line)
print(sub_child_meal.rjust(25,' '))
print(sub_child_drink.rjust(25,' '))
print(sub_child_dessert.rjust(25,' '))
print(sub_adult_meal.rjust(25,' '))
print(sub_adult_drink.rjust(25,' '))
print(sub_adult_dessert.rjust(25,' '))
print(new_line)
print(sub_t.rjust(10,' '))
print(s_tax.rjust(10,' '))
print(tot.rjust(10,' '))
print(new_line)


# Request payment amount input from user.
payment_amount      = float(input("What is the payment amount? $"))

# Calculate amount of change due after payment.
change              = payment_amount - total

# Set variable for displaying amount due.
change_amt          = (f'Change Due:  ${change:.2f}')

# Print amount of change due to user.
print(change_amt.rjust(10,' '))

# Print "Enjoy Meal" banner
print(red_bg + enjoy_banner.center(50,' ') + normal + new_line)
