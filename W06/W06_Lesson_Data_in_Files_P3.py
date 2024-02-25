# Author: Eric Arndt
# Class: CSE 110 W06 Lesson Data in Files

people = ["Stephanie 36","John 29","Emily 24","Gretchen 54","Noah 12","Penelope 32","Michael 2","Jacob 10"]
young_age = 100
print()

for person in people:
    info = person.split()
    name = info[0]
    age  = int(info[1])
    if age < young_age:
        young_age    = age
        young_person = name
    print(f"Name: {name:<12} Age: {age:^3}")

print()
print(f"Youngest is: {young_person} at age {young_age}")
print()
