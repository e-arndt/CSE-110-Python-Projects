# Author: Eric Arndt
# Class: CSE 110 W04 Word Puzzle Milestone


import random
import os


word_list = ['mosiah', 'moroni', 'mormon', 'temple', 'nephi', 'helaman', 'bountiful', 'joseph', 'benjamin', 
             'liahona', 'ordinance', 'rameumpton', 'jaredite', 'lehi', 'lamam', 'lemuel', 'zarahemla', 
             'lamanites', 'nephites', 'ammon', 'abinadi', 'alma', 'gadianton', 'cumorah', 'laban']

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

    def clrscr():
        # Check if Operating System is Mac and Linux or Windows
        if os.name == 'posix':
            _ = os.system('clear')
        else:
        # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')

    
    clrscr()
    for index in range(sw_letter_count):
        start_hint.append(start_hidden)
    print(new_line)
    print('Welcome to BoM Word Guess')
    print('Try to guess 25 BoM words')
    print(new_line)
    print(f'Hear is your hint: ',end=' ')
    print(''.join(start_hint))


    while user_guess != secret_word:

        
        print(f'{sw_letter_count} letter word.')
        user_guess = input("Enter you're guess: ").lower()
        guess_counter = (guess_counter + 1)
        stay_counter = (stay_counter + 1)
        guess_letter_count = len(user_guess)

        if not user_guess.isalpha():
            print(f"{user_guess} must contain only letters.")
            print(new_line)
            guess_counter = (guess_counter + 1)
            stay_counter = (stay_counter + 1)
            continue

        elif guess_letter_count > sw_letter_count:
            print(f"{user_guess} is too long, try again.")
            print(new_line)
            guess_counter = (guess_counter + 1)
            stay_counter = (stay_counter + 1)
            continue

        elif guess_letter_count < sw_letter_count:
            print(f"{user_guess} is too short, try again.")
            print(new_line)
            guess_counter = (guess_counter + 1)
            stay_counter = (stay_counter + 1)
            continue

        elif user_guess == secret_word:
            print(new_line)
            print(f"Your guess of {user_guess.upper()} is correct, congratulations!")
            if guess_counter >= 2:
                print(f"It took {guess_counter} guesses. ")
                print(new_line)
            else:
                print(f"It took {guess_counter} guess. ")
                print(new_line)

            run = (input('Play again? [Y/N]: '))
            if (run == "Y" or run == "y"):
                clrscr()
            elif (run != "Y" or run != "y"):
                print("Thank you for playing... Bye.")
                print(new_line)

        elif stay_counter >= 8:
                print(f"You're at {guess_counter} guesses.")
                stay = (input('Keep Playing? [Y/N]: '))
                if (stay == "Y" or stay == "y"):
                    stay_counter = 0
                    run = "Y"

                elif (stay != "Y" or stay != "y"):
                    print(f"The word was {secret_word.upper()}.")
                    print("Thank you for playing... Bye.")
                    print(new_line)
                    run = "N"
                    user_guess = secret_word

        else:
            user_hint = []
            for index in range(guess_letter_count):
            
                if user_guess[index] == secret_word[index]:
                    user_guess_letter = (user_guess[index].upper() + ' ')
                    user_hint.append(user_guess_letter)

                elif user_guess[index] in compare_letters:
                    user_guess_letter = (user_guess[index].lower() + ' ')
                    user_hint.append(user_guess_letter)
                else:
                    user_hint.append(hidden_letter)

            print (f'Hear is your hint: ',end=' ')
            print(''.join(user_hint))
            print(new_line)
