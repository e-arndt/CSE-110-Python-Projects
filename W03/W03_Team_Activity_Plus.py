# Group 18 W03 Team Project - Grade Calculator

import os
run = 'Y'

New_Line = '\n'

while (run == 'Y' or run == 'y'):
     
    os.system('cls')
    grade = int(input('Enter your grade percentage [0%-100%]: '))

    if (grade >= 90):
        letter = 'A'
        sign_num = (grade % 10)
    
    elif (grade >= 80):
        letter = 'B'
        sign_num = (grade % 10)
        
    elif (grade >= 70):
        letter = 'C'
        sign_num = (grade % 10)
        
    elif (grade >= 60):
        letter = 'D'
        sign_num = (grade % 10)
        
    else:
        letter = 'F'
        sign_num = 5

    if (sign_num >= 7):
            sign = '+'
    elif (sign_num < 3):
            sign = '-'
    else:
            sign = ' '


    if (grade >= 93):
        sign = ' '


    print(f'Your letter grade is {letter}{sign}' + New_Line)


    if (grade >=70):
        print('Congratulations on passing your class!' + New_Line)

    else:
        print("Sorry you didn't pass, next time I'm sure you will." + New_Line)

    run = (input('Run again? [Y/N]: '))
    os.system('cls')

