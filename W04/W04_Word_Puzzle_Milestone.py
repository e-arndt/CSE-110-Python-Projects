# Author: Eric Arndt
# Class: CSE 110 W04 Word Puzzle Milestone



import os
import time

new_line        = '\n'
secret_word     = 'mosiah'
guess           = '______'
sw_letter_count = len(secret_word)
hidden_letter   = '_'
guess_counter   = 0

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
        _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

def start():
    clrscr()
    print(new_line)
    print('Welcome to Word Guess')
    print(new_line)
    print (f'Hear is your hint: ',end=' ')

def length():
    global guess_counter
    guess_counter = (guess_counter + 1)
    print(new_line)
    guess = input("What's your guess? ")
    gs_letter_count = len(guess)
    if gs_letter_count < sw_letter_count:
        print(f"Sorry, {guess} is too short. Please try again.")
        time.sleep(2)
        length()
    elif gs_letter_count > sw_letter_count:
        print(f"Sorry, {guess} is too long. Please try again.")
        time.sleep(2)
        length()
    elif guess == secret_word:
        print(new_line)
        print(f"{guess} is correct. Congratulations!")
        print(f"You guessed the word in {guess_counter} tries.")
        print(new_line)
    else:
        print(f'{guess} is a good guess, but not correct,try again.')
        time.sleep(2)
        length()
       


start()

for count in range(sw_letter_count):
    sec_letter = secret_word[count]
    guess_letter = guess[count]
    if sec_letter.lower() != guess_letter.lower():
        print(hidden_letter,end=' ')
    else:
        print(sec_letter.upper(),end='')


length()






for count in range(sw_letter_count):
    
    if sec_letter.lower() != guess_letter.lower():
        print(hidden_letter,end=' ')
    elif sec_letter.lower() == guess_letter.lower():
        print(sec_letter.upper(),end='')
    else:
        print('else2')

print(new_line)

