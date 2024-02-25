# Author: Eric Arndt
# Class: CSE 110 W02 Temperature Converter
# Request temperature input, apply mathmatical conversion formula
# Display the converted temperature to the user


New_Line = '\n'

print (New_Line)


f_temp = float(input('Enter a temperature in Fahrenheit: '))


c_temp = (f_temp - 32) * 5/9


celsius = f'The temperature in Celsius is {c_temp:.1f} degrees.'


print(celsius + New_Line)

