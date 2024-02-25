# Author: Eric Arndt
# Class: CSE 110 W06 Data Analysis

import os
import time
path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\PCB 103\\CSE 110\\CSE 110 Code Projects\\W06\\life-expectancy.csv"
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
highest_life        = -1
year_highest_life   = -1
year_sum            = 0
count               = 0
year_search         = []

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

    def prtscn():
        print(new_line)
        print(f"The overall MAX life expectancy is: {highest_life:.2f} years from {highest_country} in {highest_year}")
        print(f"The overall MIN life expectancy is: {lowest_life:.2f} years from {lowest_country} in {lowest_year}")
        print(new_line)
        print(f"Report for {search_year}")
        print(f"The average life expectancy across all countries was: {year_exp_avg:.2f}")
        print(f"The MAX life expectancy was in {year_highest_country} with {year_highest_life:.2f}")
        print(f"The Min life expectancy was in {year_lowest_country} with {year_lowest_life:.2f}")
        print(new_line)
        


    def menu():
        clrscr()
        print(red_bd + main_banner.center(50,' '))
        print(red_bd + mid_banner.center(50,' '))
        print(red_bd + low_banner.center(50,' ') + normal + new_line)


    menu()
    year_search.clear()
    year_sum = 0
    year_exp_avg = 0
    count = 0
    year_lowest_life    = 999
    year_highest_life   = -1
    year_lowest_country = ""
    year_lowest_year    = 0
    highest_life = 0
    highest_country = ""
    highest_year = 0
    search_year = (input("Enter a search year: "))

    if search_year.isalpha():
        print("Please enter only numbers. 4 digit year [yyyy].")
        time.sleep(3)
        menu()
    elif int(search_year) < 1543 or int(search_year) > 2019:
        print("That year is not available.")
        time.sleep(2)
        menu()
    elif int(search_year) >= 1543 or int(search_year) <= 2019:
        with open(path, "r") as expectancy_data:

            header = next(expectancy_data)

            for expectancy in expectancy_data:
                life_record   = expectancy.strip()
                life_record   = expectancy.split(",")
                country_name  = life_record[0]
                country_code  = life_record[1]
                data_year     = life_record[2]
                life_expect   = float(life_record[3])
                if search_year == data_year:
                    year_search.append(life_expect)
                    if life_expect < year_lowest_life:
                        year_lowest_life    = life_expect
                        year_lowest_country = country_name
                        year_lowest_year    = data_year
                        
                    if life_expect > year_highest_life:
                        year_highest_life = life_expect
                        year_highest_country = country_name
                        year_highest_year = data_year

                if life_expect < lowest_life:
                    lowest_life    = life_expect
                    lowest_country = country_name
                    lowest_year    = data_year

                if life_expect > highest_life:
                    highest_life = life_expect
                    highest_country = country_name
                    highest_year = data_year
                    

            count = (len(year_search))
            if count == 0:
                print(f"No data available for {search_year}.")
                search_year = ""
                time.sleep(2)
                menu()

            else:
                for exp in range(len(year_search)):
                    year_sum = (year_sum + (year_search[exp]))
                year_exp_avg = (year_sum / count)
                prtscn()

    else:
        menu()
    
    
    run = input("Search again? [Y/N]")

if (run == "Y" or run == "y"):
    year_search.clear()
    year_sum = 0
    year_exp_avg = 0
    count = 0
    year_lowest_life    = 999
    year_lowest_country = ""
    year_lowest_year    = 0
    highest_life = 0
    highest_country = ""
    highest_year = 0
    clrscr()
elif (run != "Y" or run != "y"):
    clrscr()
    print(new_line)
    print("Bye...")
    print(new_line)