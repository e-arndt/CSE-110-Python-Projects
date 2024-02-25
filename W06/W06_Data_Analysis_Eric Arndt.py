# Creativity:
# Created a banner to identify the search function, provide valid year range and notify user of some missing years below 1751
# Added the ability to search by country.
# Added the option to run the search again or quit.
# Capitalize the name of the country in the report even if user enters lowercase.
# Added some error handling to deal with invalid user inputs.
# Added handling of years and country names not in the data file.

# Author: Eric Arndt
# Class: CSE 110 W06 Data Analysis

# Import libraries
import os
import time

# Set the variable "path" to the drive and folder location of the data file
path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\PCB 103\\CSE 110\\CSE 110 Code Projects\\W06\\life-expectancy.csv"

# Set variables and list
esc                 = '\x1b'
red_bd              = esc + '[41m'
normal              = esc + '[0m'
new_line            = "\n"
main_banner         = "SPANISH FLU LIFE EXPECTANCY DATA SEARCH"
mid_banner          = "DATA RANGE 1543 - 2019"
low_banner          = "BELOW 1751 DATA LIMITED OR NOT AVAILABLE"
run                 = "Y"
lowest_life         = 999
year_lowest_life    = 999
ctry_lowest_life    = 999
highest_life        = -1
year_highest_life   = -1
ctry_highest_life   = -1
year_sum            = 0
ctry_sum            = 0
count               = 0
user_search         = []

# Main while loop, runs until user quits
while run == "Y" or run == "y":

# Set function for clearing terminal screen
    def clrscr():
    # Check if Operating System is Mac and Linux
        if os.name == 'posix':
            _ = os.system('clear')
        else:
    # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')

    # Define function to print report based on year
    def prt_year():
        print(new_line)
        print(f"The overall MAX life expectancy is: {highest_life:.2f} years from {highest_country} in {highest_year}")
        print(f"The overall MIN life expectancy is: {lowest_life:.2f} years from {lowest_country} in {lowest_year}")
        print(new_line)
        print(f"Report for {search}")
        print(f"The AVG life expectancy across all countries that year was: {year_exp_avg:.2f}")
        print(f"The MAX life expectancy was in {year_highest_country} with {year_highest_life:.2f}")
        print(f"The MIN life expectancy was in {year_lowest_country} with {year_lowest_life:.2f}")
        print(new_line)
        
    # Define function to print report based on country
    def prt_ctry():
        print(new_line)
        print(f"The overall MAX life expectancy is: {highest_life:.2f} years from {highest_country} in {highest_year}")
        print(f"The overall MIN life expectancy is: {lowest_life:.2f} years from {lowest_country} in {lowest_year}")
        print(new_line)
        print(f"Report for {search.title()}")
        print(f"The AVG life expectancy for all years is: {ctry_exp_avg:.2f}")
        print(f"The MAX life expectancy was in {ctry_highest_year} with {ctry_highest_life:.2f}")
        print(f"The MIN life expectancy was in {ctry_lowest_year} with {ctry_lowest_life:.2f}")
        print(new_line)

    # Define function to print informational banner on main screen
    def menu():
        clrscr()
        print(red_bd + main_banner.center(50,' '))
        print(red_bd + mid_banner.center(50,' '))
        print(red_bd + low_banner.center(50,' ') + normal + new_line)
        
    # Call menu function and reset variables
    menu()
    user_search.clear()
    year_sum            = 0
    ctry_sum            = 0
    year_exp_avg        = 0
    count               = 0
    year_lowest_life    = 999
    year_highest_life   = -1
    year_lowest_country = ""
    year_lowest_year    = 0
    highest_life        = 0
    highest_country     = ""
    highest_year        = 0
    # Request search year or country name from user
    search = (input("Enter a search year or country name: "))

    # while user search is not a numerical year do the following
    while not search.isnumeric():
        # open data file and assign it the variable expectancy_data
        with open(path, "r") as expectancy_data:

            # Read the first line of data from the file and store in the variable "header" then move to the next line of data
            header = next(expectancy_data)

            # Loop to step through each line of data in the file
            for expectancy in expectancy_data:
                # Strip off whitespaces in data string
                life_record   = expectancy.strip()
                # Split string of data into separate parts by looking for a ","
                life_record   = expectancy.split(",")
                # Assign variables to each part of the split data
                country_name  = life_record[0]
                country_code  = life_record[1]
                data_year     = life_record[2]
                life_expect   = float(life_record[3])
                # if the user search term equals the country name, perform the following
                if search.lower() == (country_name.lower()):
                    # Append that country's data to the data list called "user_search"
                    user_search.append(life_expect)
                    # search for and save into variables, the lowest life expectancy for the search country
                    if life_expect < ctry_lowest_life:
                        ctry_lowest_life    = life_expect
                        ctry_lowest_country = country_name
                        ctry_lowest_year    = data_year

                    # search for and save into variables, the highest life expectancy for the search country
                    if life_expect > ctry_highest_life:
                        ctry_highest_life = life_expect
                        ctry_highest_country = country_name
                        ctry_highest_year = data_year

                # search for and save into variables the country with the overall lowest life expectancy
                if life_expect < lowest_life:
                    lowest_life    = life_expect
                    lowest_country = country_name
                    lowest_year    = data_year

                # search for and save into variables the country with the overall highest life expectancy
                if life_expect > highest_life:
                    highest_life = life_expect
                    highest_country = country_name
                    highest_year = data_year
                    
            # Count the length of the user_search list. If nothing has been added to the list and the count is 0, report no data
            count = (len(user_search))
            if count == 0:
                print(f"No data available for {search}.")
                time.sleep(2)
                run = "Y"
                break
            # Otherwise use the data in the user_search list to calculate the country's average life expectancy
            else:
                for exp in range(len(user_search)):
                    ctry_sum = (ctry_sum + (user_search[exp]))
                ctry_exp_avg = (ctry_sum / count)
                prt_ctry()
                run = input("Search again? [Y/N]")
                break


    # while user search is a numerical year do the following            
    while search.isdecimal():
        # try this code first
        try:
            # if user input is outside of range of valid years
            if int(search) < 1543 or int(search) > 2019:
                print("That year is not available.")
                time.sleep(2)
                run = "Y"
                break
        # If the user input generates an error then do the following
        except ValueError:
            print("That is not a valid entry.")
            time.sleep(2)
            run = "Y"
            break
        
        # try this code first
        try:
            # If user input is within the valid range of years
            if int(search) >= 1543 or int(search) <= 2019:
                # open data file and assign it the variable expectancy_data
                with open(path, "r") as expectancy_data:
                    
                    # Read the first line of data from the file and store in the variable "header" then move to the next line of data
                    header = next(expectancy_data)

                    # Loop to step through each line of data in the file
                    for expectancy in expectancy_data:
                        # Strip off whitespaces in data string
                        life_record   = expectancy.strip()
                        # Split string of data into separate parts by looking for a ","
                        life_record   = expectancy.split(",")
                        # Assign variables to each part of the split data
                        country_name  = life_record[0]
                        country_code  = life_record[1]
                        data_year     = life_record[2]
                        life_expect   = float(life_record[3])
                        # if the user search term equals the data year, perform the following
                        if search == data_year:
                            # Append that year's data to the data list called "user_search"
                            user_search.append(life_expect)
                            # search for and save into variables, the lowest life expectancy for the search year
                            if life_expect < year_lowest_life:
                                year_lowest_life    = life_expect
                                year_lowest_country = country_name
                                year_lowest_year    = data_year
                                
                            # search for and save into variables, the highest life expectancy for the search year
                            if life_expect > year_highest_life:
                                year_highest_life = life_expect
                                year_highest_country = country_name
                                year_highest_year = data_year

                        # search for and save into variables the country with the overall lowest life expectancy
                        if life_expect < lowest_life:
                            lowest_life    = life_expect
                            lowest_country = country_name
                            lowest_year    = data_year

                        # search for and save into variables the country with the overall highest life expectancy
                        if life_expect > highest_life:
                            highest_life = life_expect
                            highest_country = country_name
                            highest_year = data_year
                            
                    # Count the length of the user_search list. If nothing has been added to the list and the count is 0, report no data
                    count = (len(user_search))
                    if count == 0:
                        print(f"No data available for {search}.")
                        time.sleep(2)
                        run = "Y"
                        break

                    # Otherwise use the data in the user_search list to calculate the year's average life expectancy
                    else:
                        for exp in range(len(user_search)):
                            year_sum = (year_sum + (user_search[exp]))
                        year_exp_avg = (year_sum / count)
                        prt_year()
                        run = input("Search again? [Y/N]")
                        break
    
        # If the user input generates an error then do the following
        except ValueError:
            print("That is not a valid entry.")
            time.sleep(2)
            run = "Y"
            break

# If "run" equals Y or y then continue the while loop and the program, reset variables to rerun the program fresh
if (run == "Y" or run == "y"):
    user_search.clear()
    year_sum            = 0
    ctry_sum            = 0
    year_exp_avg        = 0
    count               = 0
    year_lowest_life    = 999
    year_lowest_country = ""
    year_lowest_year    = 0
    highest_life        = 0
    highest_country     = ""
    highest_year        = 0
    search              = ""
    clrscr()

# if "run" doesn't equal Y or y then say bye and end program
elif (run != "Y" or run != "y"):
    clrscr()
    print(new_line)
    print("Bye...")
    print(new_line)