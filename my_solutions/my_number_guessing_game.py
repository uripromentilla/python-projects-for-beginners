# A Game where the user has to guess a number between 1 and 100

import random

# The game randomly generates a number between 1 and 100 for the user to guess.
target = random.randint(1, 100)

# While the user has not guessed the number correctly, the game will keep asking for input.
while True:
    # The user is prompted to enter a number between 1 and 100.
    guess = input("Guess a number between 1 and 100: ")

    # Check if the input can be converted to an integer.
    try:
        guess = int(guess)
        # If anything else that is not a number from 1 to 100 is entered, the user is prompted to enter a valid number.
        if guess not in range(1, 101):
            print("Please enter a valid number.")
        # If the entered number is too high, the program prints "Too high!"
        elif guess > target:
            print("Too high!")
        # If the entered number is too low, the program prints "Too low!"
        elif guess < target:
            print("Too low!")
        # If the entered number is correct, the program prints "Congratulations! You guessed the number."
        elif guess == target:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number.")
