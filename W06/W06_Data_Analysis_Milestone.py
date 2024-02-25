# Author: Eric Arndt
# Class: CSE 110 W06 Data Analysis Milestone

# Import library
import os

# Set data file path
path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\PCB 103\\CSE 110\\CSE 110 Code Projects\\W06\\life-expectancy.csv"

# Set initial variable values
lowest_life = 999
highest_life = -1


# Set function for clearing terminal screen
def clrscr():
    # Check if Operating System is Mac and Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')

# Call clear screen function
clrscr()

# Open data file in Read Mode, specifying "r" as a visual cue only since "with open" with no parameter also opens in "read mode"
with open(path, "r") as expectancy_data:

# Assign first line of data file, the header, to a variable, setting the next line of actual data to be read.
    header = next(expectancy_data)

# Loop to read data from the data file
    for expectancy in expectancy_data:
        # Strip off leading and trailing spaces from data
        life_record = expectancy.strip()
        # Split the now stripped data into separate parts
        life_record = expectancy.split(",")
        # First data part (name) assigned to variable
        country_name  = life_record[0]
        # Second data part (country code) assigned to variable
        country_code  = life_record[1]
        # Third data part (year) assigned to variable
        data_year     = life_record[2]
        # Fourth data part (life expectancy) assigned to variable
        life_expect   = float(life_record[3])

        # Find lowest life expectancy from data file
        if life_expect < lowest_life:
            lowest_life = life_expect

        # Find highest life expectancy from data file
        if life_expect > highest_life:
            highest_life = life_expect

# Print highest and lowest expectancies found
print()
print(f"Highest Life Expectancy: {highest_life}")
print(f"Lowest Life Expectancy : {lowest_life}")
print()
print()
