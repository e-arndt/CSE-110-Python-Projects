import random

# List of possible secret words
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Select a random word from the list
secret_word = random.choice(words)
#secret_word = 'parts'
# Generate a set of the unique letters in the secret word
unique_letters = set(secret_word)

# Define the maximum number of guesses
max_guesses = 6
num_guesses = 0

# Start the game loop
while num_guesses < max_guesses:
    # Print the number of remaining guesses
    print("You have", max_guesses - num_guesses, "guesses left.")

    # Prompt the user for a guess
    guess = input(f"Guess a {len(secret_word)} letter word: ")
    num_guesses += 1

    # Check if the guess is valid
    if len(guess) != len(secret_word):
        print("Your guess should have exactly " + len(secret_word) + " letters.")
        continue
    if not guess.isalpha():
        print("Your guess should only contain letters.")
        continue

    # Check if the guess is correct
    if guess == secret_word:
        print("Congratulations, you guessed the word!")
        break

    # Generate the hint for the user
    hint = []
    for j in range(len(secret_word)):
        if guess[j] == secret_word[j]:
            hint.append(guess[j].upper())
        elif guess[j] in unique_letters:
            hint.append(guess[j].lower())
        else:
            hint.append(' _ ')

    # Print the hint to the user
    print(''.join(hint))

# If the user runs out of guesses, reveal the secret word
if num_guesses == max_guesses:
    print("Sorry, you ran out of guesses. The word was", secret_word)
