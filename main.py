# Changhong Wen
# 10/9/2024
# Purpose: Create a game that allows players to guess a number.

import random

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("Try to guess it! Type 'q' to quit at any time.")

# Generate a random number between 1 and 100
number = random.randint(1,100)

# Initialize the guess counter
guess_count = 0

# Jump into an infinite loop, for testing
while True:

    # Get the player's guess as a string first
    player_guess = input("Enter your guess: ")

    # Allow the player to quit the game
    if player_guess.lower() == 'q':  # Check if the input is 'q'
        print("You've decided to quit the game.")
        print("q Thanks for playing!")
        break

    # Convert the player's input to an integer, handle invalid inputs
    try:
        player_guess = int(player_guess)
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
        continue

    # Nicely fail if we have a value error

    except ValueError as e:
        print(f"It appears that input is not between 1 and 100")
        print(f"\t{e}")



    # Increase the guess counter
    guess_count = guess_count + 1

    # Check if the guess is correct, too high, or too low
    if player_guess < number:
        print("Your guess is too low. Try again!")
    elif player_guess > number:
        print("Your guess is too high. Try again!")
    else:
        print(f"Good job! You guessed the correct number {number} in {guess_count} guesses.")
        break
