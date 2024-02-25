# Author: Eric Arndt
# Class: CSE 110 W06 Team Activity HR 4 Stretch

# Set path to data file
path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\PCB 103\\CSE 110\\CSE 110 Code Projects\\W06\\hr_system.txt"
# Add a line for spacing
print()

# Open file in read "r" mode
with open(path, "r") as employee_data:

# Create for loop to read each line of data in file
    for employee in employee_data:
        # Strip off blank spaces / hidden characters
        emp_record = employee.strip()
        # Split line of data into separate parts
        emp_record = employee.split()
        # Set variable to each part of data
        emp_name   = emp_record[0]
        emp_id_num = emp_record[1]
        emp_job    = emp_record[2]
        # Set emp_salary data as an integer rather than string data
        emp_salary = int(emp_record[3])
        # Set paycheck to bi-weekly pay amount
        paycheck   = (emp_salary / 24)
        # If job title equals "Engineer" give a $1000 bonus per paycheck
        if emp_job == "Engineer":
            paycheck += 1000

        # Print data to screen, spaced in columns for easy reading
        print(f"Name: {emp_name:<12} (ID: {emp_id_num:^4}),   Title: {emp_job:<10} -  ${paycheck:.2f}")
        
print()