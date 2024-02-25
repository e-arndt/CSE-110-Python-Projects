# Author: Eric Arndt
# Class: CSE 110 W06 Team Activity HR 1


path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\PCB 103\\CSE 110\\CSE 110 Code Projects\\W06\\hr_system.txt"
print()
with open(path, "r") as emp_data:
    for emp in emp_data:
        record = emp.strip()
        print(record)
        
print()