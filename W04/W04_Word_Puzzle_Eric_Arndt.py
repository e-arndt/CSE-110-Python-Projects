# Creativity:
# Increased secret words to 25, secret words are randomly selected.
# Restate user input on incorrect guesses rather than just saying, your guess is not correct.
# Added option to give up or continue after about 8+ incorrect guesses, this includes incorrect length guesses.
# Overall guess counter displayed to user is not affected. Secret word is revealed after giving up.
# Added option to play the game again or quit after successful guess.

# Author: Eric Arndt
# Class: CSE 110 W04 Word Puzzel Game

# Set import libraries for random function, OS type check and time / wait / sleep function.
import random
import os
import time

# Set word list
word_list = ['mosiah', 'moroni', 'mormon', 'temple', 'nephi', 'helaman', 'bountiful', 'joseph', 'benjamin', 
             'liahona', 'ordinance', 'rameumpton', 'jaredite', 'lehi', 'lamam', 'lemuel', 'zarahemla', 
             'lamanites', 'nephites', 'ammon', 'abinadi', 'alma', 'gadianton', 'cumorah', 'laban']

# Set static and initial variable values.
run                     = "Y"
stay                    = "N"
while run == "Y" or run == "y":
    new_line            = '\n'
    secret_word         = random.choice(word_list)
    sw_letter_count     = len(secret_word)
    guess_letter_count  = 0
    hidden_letter       = ' _ '
    guess_counter       = 0
    stay_counter        = 0
    user_guess          = ''
    user_hint           = []
    compare_letters     = set(secret_word)
    start_hint          = []
    start_hidden        = ('_ ')

# Set function for initial start procedures
    def start():
        clrscr()
        print('Selecting Secret Word.....')
        time.sleep(2)

# Set function for clearing terminal screen
    def clrscr():
        # Check if Operating System is Mac and Linux
        if os.name == 'posix':
            _ = os.system('clear')
        else:
        # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')

# Call functions, initial program start, build and display first hint
    start()
    clrscr()
    for index in range(sw_letter_count):
        start_hint.append(start_hidden)
    print('Welcome to BoM Word Guess')
    print('Guess from 25 BoM words')
    print(new_line)
    print(f'Hear is your hint: ',end=' ')
    print(''.join(start_hint))

# While user guess does not equal the secret word, continue the loop
    while user_guess != secret_word:

# Give letter count of secret word, request user input for guess, find length of user guess for comparison
        print(f'{sw_letter_count} letter word.')
        user_guess = input("Enter you're guess: ").lower()
        guess_letter_count = len(user_guess)

# User input must include letters only, advance "stay" counter
        if not user_guess.isalpha():
            print(f"{user_guess} must contain only letters.")
            print(new_line)
            stay_counter = (stay_counter + 1)
            continue

# User input can't be longer than secret word, advance "stay" counter
        elif guess_letter_count > sw_letter_count:
            print(f"{user_guess} is too long, try again.")
            print(new_line)
            stay_counter = (stay_counter + 1)
            continue

# User input can't be shorter than secret word, advance "stay" counter
        elif guess_letter_count < sw_letter_count:
            print(f"{user_guess} is too short, try again.")
            print(new_line)
            stay_counter = (stay_counter + 1)
            continue

# If user guess equals the secret word, display congrats, guess counter and ask user to play again or quit.
        elif user_guess == secret_word:
            guess_counter = (guess_counter + 1)
            stay_counter = (stay_counter + 1)
            print(new_line)
            print(f"Your guess of {user_guess.upper()} is correct, congratulations!")
            # If guess counter is 2 or more use plural form of sentence
            if guess_counter >= 2:
                print(f"It took {guess_counter} guesses. ")
                print(new_line)
            # Otherwise if guess counter is less than 2 use singular form of sentence    
            else:
                print(f"It took {guess_counter} guess. ")
                print(new_line)
            # Ask user to play again or quit
            run = (input('Play again? [Y/N]: '))
            if (run == "Y" or run == "y"):
                clrscr()
            elif (run != "Y" or run != "y"):
                print("Thank you for playing... Bye.")
                print(new_line)

# If user guesses reach 8 or more before guessing the secret word, give option to quit or continue playing.
# Keep playing resets the "stay" counter but not overall guess counter.
        elif stay_counter >= 8:
                stay_counter = (stay_counter + 1)
                guess_counter = (guess_counter + 1)
                print(f"You're at {stay_counter} attempts.")
                stay = (input('Keep Playing? [Y/N]: '))
                if (stay == "Y" or stay == "y"):
                    stay_counter = 0
                    print(new_line)
                    run = "Y"

# If user quits, secret word is displayed and game ends.
                elif (stay != "Y" or stay != "y"):
                    print(f"The word was {secret_word.upper()}.")
                    print("Thank you for playing... Bye.")
                    print(new_line)
                    run = "N"
                    user_guess = secret_word

# else the guessing / clue process continues, user_hint set as an empty list, counters increase, for loop set
        else:
            user_hint = []
            guess_counter = (guess_counter + 1)
            stay_counter = (stay_counter + 1)
            for index in range(guess_letter_count):
# for as long as the word is, each letter is tested and written to "user_hint", cap letters for correct
                if user_guess[index] == secret_word[index]:
                    user_guess_letter = (user_guess[index].upper() + ' ')
                    user_hint.append(user_guess_letter)
# if not correct, tested if at least present in list of letters from secret word, if true, written to user_hint as lowercase.
                elif user_guess[index] in compare_letters:
                    user_guess_letter = (user_guess[index].lower() + ' ')
                    user_hint.append(user_guess_letter)
# else if both false then an underline character "_" is written to user_hint for that letter.
                else:
                    user_hint.append(hidden_letter)

# print the result from user_hint, but first "join" the letters together from a "list" of letters into a string
            print (f'Hear is your hint: ',end=' ')
            print(''.join(user_hint))
            print(new_line)
