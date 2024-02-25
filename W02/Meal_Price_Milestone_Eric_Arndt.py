# Author: Eric Arndt
# Class: CSE 110 W02 Meal Price Calculator
# Request price, quantity, tax an payment inputs, calculate subtotal, tax, total and change due.
# Display calculated data to user.

# Set variable to command for a new line
new_line         = '\n'

# Request input from user for meal prices and number of meals.
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_of_children  = int(input("How many children are there? "))
num_of_adults    = int(input("How many adults are there? "))
sales_tax_rate   = float(input('What is the current sales tax rate? '))

# Calculate subtotals and toals, store the resaults in variables.
child_meal_sub   = (child_meal_price * num_of_children)
adult_meal_sub   = (adult_meal_price * num_of_adults)
sub_total        = (child_meal_sub + adult_meal_sub)
sales_tax        = sub_total * (sales_tax_rate / 100)
total            = sub_total + sales_tax

# Set variables to desired output format.
sub_t            = (f'Subtotal:   ${sub_total:.2f}')
s_tax            = (f'Sales Tax:   ${sales_tax:.2f}')
tot              = (f'Total:      ${total:.2f}')

# Print a new line for spacing. Print subtotal.
print(new_line)
print(sub_t.rjust(10,' '))


