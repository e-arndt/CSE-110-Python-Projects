# Group 18 Team Project - Grade Calculator


New_Line               = '\n'

print(New_Line)
grade_percent = int(input('Enter your grade percentage [0%-100%]: '))

if (grade_percent >= 90):
    letter = 'A'

elif (grade_percent >= 80):
    letter = 'B'

elif (grade_percent >= 70):
    letter = 'C'

elif (grade_percent >= 60):
    letter = 'D'

else:
    letter = 'F'


print(f'Your letter grade is {letter}' + New_Line)


if (grade_percent >=70):
    print('Congratulations on passing your class!' + New_Line)

else:
    print("Sorry you didn't pass, next time I'm sure you will." + New_Line)
