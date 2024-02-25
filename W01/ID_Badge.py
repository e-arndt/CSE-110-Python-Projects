# Author: Eric Arndt
# Class: CSE 110 W01 Individual Activity: ID Badge Generator
# Request data input form employee, create an ID Badge by displaying data in a specificed format

# Request user to input required data
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
email = input('What is your email address? ')
phone = input('What is your phone number? ')
job_title = input('What is your job title? ')
id_num = input('What is your ID number? ')

# Set variable "space" to \n for line spacing
space = '\n'

# Set variable "ID_Border" to "-" to create outline of ID Badge
ID_Border = ('---------------------------------------------')

# Set "Line" variables to desired ID Badge format for each line of badge
Line1 = f'{last_name.upper()}, {first_name.capitalize()}'
Line2 = f'{job_title.title()}'
Line3 = f'ID: {id_num}'
Line4 = f'{email.lower()}'
Line5 = f'{phone}'

# Create ID Card output on screen
print(space)
print('The ID Card is:')
print(ID_Border)
print(Line1)
print(Line2)
print(Line3)
print()
print(Line4)
print(Line5)
print(ID_Border)
print(space)
