# Group 18 Team Project - Grade Calculator


New_Line               = '\n'

print(New_Line)
grade_percent = int(input('Enter your grade percentage [0%-100%]: '))

if (grade_percent >= 90):
    print('Your letter grade is A' + New_Line)

elif (grade_percent >= 80):
    print('Your letter grade is B' + New_Line)

elif (grade_percent >= 70):
    print('Your letter grade is C' + New_Line)

elif (grade_percent >= 60):
    print('Your letter grade is D' + New_Line)

else:
    print('Your letter grade is F' + New_Line)


if (grade_percent >=70):
    print('Congratulations on passing your class!' + New_Line)

else:
    print("Sorry you didn't pass, next time I'm sure you will." + New_Line)

