# Author: Eric Arndt
# Class: CSE 110 W02 Meal Price Calculator
# Request price, quantity, tax an payment inputs, calculate subtotal, tax, total and change due.
# Display calculated data to user.

NL               = '\n'
ESC              = '\x1b'
RED_BG           = ESC + '[41m'
NORMAL           = ESC + '[0m'
WELCOME_BANNER   = "WELCOME TO BUFFY'S BUFFET"
ENJOY_BANNER     = "ENJOY YOUR MEAL "




print(RED_BG + WELCOME_BANNER.center(50,' ') + NORMAL + NL)


child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_of_children  = int(input("How many children are there? "))
num_of_adults    = int(input("How many adults are there? "))
sales_tax_rate   = float(input('What is the current sales tax rate? '))


child_meal_sub   = (child_meal_price * num_of_children)
adult_meal_sub   = (adult_meal_price * num_of_adults)
sub_total        = (child_meal_sub + adult_meal_sub)
sales_tax        = sub_total * (sales_tax_rate / 100)
total            = sub_total + sales_tax

sub_t            = (f'Subtotal:   ${sub_total:.2f}')
s_tax            = (f'Sales Tax:   ${sales_tax:.2f}')
tot              = (f'Total:      ${total:.2f}')


print(NL)
print(sub_t.rjust(10,' '))
print(s_tax.rjust(10,' '))
print(tot.rjust(10,' '))
print(NL)

payment_amount   = float(input("What is the payment amount? $"))
change           = payment_amount - total
change_amt       = (f'Change Due:  ${change:.2f}')

print(change_amt.rjust(10,' '))

print(RED_BG + ENJOY_BANNER.center(50,' ') + NORMAL + NL)
