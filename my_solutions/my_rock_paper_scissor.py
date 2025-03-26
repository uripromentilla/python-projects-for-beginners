# A game of rock paper scissors between the user and the computer.

import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

# Map the choices to an emoji.
rps_dict = {
    ROCK: "🪨",
    PAPER: "📃",
    SCISSORS: "✂️",
}

choices = tuple(rps_dict.keys())


def get_user_choice():
    while True:
        # Ask the user for their choice. The user can choose 'r' for rock, 'p' for paper, or 's' for scissors.
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        # If the user enters anything else, print "Invalid choice!" Continue to ask them until they enter a valid choice.
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


def display_choices(user_choice, computer_choice):
    # Print the user's choice.
    print(f"You chose {rps_dict[user_choice]}")
    # Print the computer's choice.
    print(f"Computer chose {rps_dict[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    # Evaluate the user's choice against the computer's choice.
    # Print the result of the game.
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == SCISSORS and computer_choice == PAPER)
        or (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You win!")
    else:
        print("You lose!")


def play_game():
    while True:
        # Get the user's choice.
        user_choice = get_user_choice()

        # Generate a random choice for the computer. The computer can choose 'r' for rock, 'p' for paper, or 's' for scissors.
        computer_choice = random.choice(list(rps_dict.keys()))

        # Print the user's choice and the computer's choice.
        display_choices(user_choice, computer_choice)

        # Determine the winner.
        determine_winner(user_choice, computer_choice)

        # print(user_choice)
        # print(computer_choice)

        # Ask the user if they want to continue.
        continue_game = input("Do you want to continue? (y/n): ").lower()
        # If the user enters 'n', exit the loop.
        if continue_game == "n":
            break


play_game()
