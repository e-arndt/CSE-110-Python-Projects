# Author: Eric Arndt
# Class: CSE 110 W06 Team Activity HR 2


path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\PCB 103\\CSE 110\\CSE 110 Code Projects\\W06\\hr_system.txt"
print()

with open(path, "r") as employee_data:

    for employee in employee_data:
        emp_record = employee.strip()
        emp_record = employee.split()
        emp_name   = emp_record[0]
        emp_id_num = emp_record[1]
        emp_job    = emp_record[2]
        emp_salary = emp_record[3]

        print(emp_name)
        
print()