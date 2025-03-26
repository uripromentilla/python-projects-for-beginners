# Dice Rolling Game

import random

# Repeat until the user inputs 'n'
while True:
    # Ask the user if they want to roll the dice
    choice = input("Roll the dice? (y/n): ").lower()

    # If the user inputs 'y', roll two dice and print the results.
    # If the user inputs 'n', print a message thanking them for playing.
    # If the user inputs anything else, print an error message.
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
