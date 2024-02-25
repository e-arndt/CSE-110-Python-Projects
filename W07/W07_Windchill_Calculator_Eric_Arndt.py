# Creativity:
# Created individual screens with banners labeling the function or current screen viewed.
# Added some error handeling of invalid user inputs.
# Formatted the text output to look uniform and easier to read.

# Author: Eric Arndt
# Class: CSE 110 W07 Windchill Calculator

# Import library
import os
import time

# Set initial variable values
new_line     = '\n'
run          = "run"
esc          = '\x1b'
red_bd       = esc + '[41m'
normal       = esc + '[0m'
main_banner  = "WINDCHILL CALCULATOR"
chill_banner = "WINDCHILL CHART"


# Set function for clearing terminal screen
def clrscr():
    # Check if Operating System is Mac and Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')

# Function to convert Celsius to Fahrenheit
def convert_c_f(celsius):
    fahrenheit = (celsius * (9/5) + 32)
    return fahrenheit


# Function to calculate windchill
def windchill_calc(temp, wind):
    windchill = (35.74 + (0.6215 * temp) - (35.75 * (wind ** 0.16)) + (0.4275 * temp) * (wind ** 0.16))
    return windchill



# while loop until user quits
while run != "n":
    # clear screen
    clrscr()
    # print screen banner
    print(red_bd + main_banner.center(50,' ') + normal + new_line)
    # try this code until error occurs
    try:
        # user inputs F for Fahrenheit or C for Celsius
        c_or_f = input("Fahrenheit or Celsius [F/C] ")
        # if user input = F then execute the following code
        if c_or_f.lower() == "f":
            # prompt user for temperature in Fahrenheit
            user_temp = float(input("Enter temperature: "))
            clrscr()
            # banner for windchill chart
            print(red_bd + chill_banner.center(50,' ') + normal + new_line)
            # loop from 5 to 60 step by 5 for wind in mph (5 - 60 mph)
            for v in range(5, 61, 5):
                # set variable = to the return of function called windchill_calc,
                # pass the temperature and wind speed value to the function for calculation
                chill = windchill_calc(temp = user_temp, wind = v)
                # print the resulting calculations from the function to the user
                print(f"{user_temp:<3}F, wind speed of {v:^2} mph, windchill is: {chill:.2f}F")
            # Run again?
            print(new_line)
            rerun = input("Run Again? [Y/N]")
            if rerun.lower() == "y":
                run = "run"
            else:
                print(new_line)
                print("Bye...")
                print(new_line)
                run = "n"

        # if user input = C then execute the following code
        elif c_or_f.lower() == "c":
            # prompt user for temperature in Celsius
            user_temp = float(input("Enter temperature: "))
            # set variable = to the return of function called convert_c_f,
            # pass the Celsius temperature from the user to the function for conversion
            fahrenheit = convert_c_f(celsius = user_temp)
            clrscr()
            # banner for windchill chart
            print(red_bd + chill_banner.center(50,' ') + normal + new_line)
            # loop from 5 to 60 step by 5 for wind in mph (5 - 60 mph)
            for v in range(5, 61, 5):
                # set variable = to the return of function called windchill_calc,
                # pass the temperature and wind speed value to the function for calculation
                chill = windchill_calc(temp = fahrenheit, wind = v)
                # print the resulting calculations from the function to the user
                print(f"{fahrenheit:<3}F, wind speed of {v:^2} mph, windchill is: {chill:.2f}F")
            # Run again?
            print(new_line)
            rerun = input("Run Again? [Y/N]")
            if rerun.lower() == "y":
                run = "run"
            else:
                print(new_line)
                print("Bye...")
                print(new_line)
                run = "n"

        # if not C or F then the user entry is invalid
        else:
            print("Invalid entry")
            time.sleep(2)
            run = "run"
            continue

    # handles any other invalid input errors
    except ValueError:
            print("Invalid entry.")
            time.sleep(2)
            run = "run"
            continue
    