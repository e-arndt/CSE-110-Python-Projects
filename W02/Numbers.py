# Author: Eric Arndt
# Class: CSE 110 W02 Individual Activity: Numbers
# Request data input form user, convert data to number, display data in a specificed format for the user.

# Set static variables
NEW_LINE         = '\n'
ESC              = '\x1b'
RED_BG           = ESC + '[41m'
NORMAL_TEXT      = ESC + '[0m'
print(NEW_LINE)

# Variables set for input from user.
# Variable name, input prompt, description of type of input requested.
User_Age        = int(input('How old are you? '))


Age             = (User_Age) +1

Birthday_Age    = f'On your next birthday, you will be {Age} years old.'

print(Birthday_Age + NEW_LINE)


# Variables set for input from user.
# Variable name, input prompt, description of type of input requested.
User_Cartons    = int(input('How many egg cartons do you have? '))


Eggs            = (User_Cartons) *12

Total_Eggs    = f'You have a total of {Eggs} eggs.'

print(Total_Eggs + NEW_LINE)


# Variables set for input from user.
# Variable name, input prompt, description of type of input requested.
User_Cookies    = int(input('How many cookies do you have? '))
User_People     = int(input('How many people are there? '))

Cookies             = (User_Cookies) / (User_People)

Cookies_per    = f'Each person may have {Cookies} cookies.'

print(Cookies_per + NEW_LINE)
