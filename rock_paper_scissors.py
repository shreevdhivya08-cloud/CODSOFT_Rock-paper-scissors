"""
Rock-Paper-Scissors Game
-------------------------
A command-line game where the user plays Rock-Paper-Scissors against
the computer across multiple rounds, with score tracking and replay support.

Author: Generated with Claude
"""

import random

# Valid choices for the game, stored once so we can reuse/validate against them
VALID_CHOICES = ("rock", "paper", "scissors")

# Maps each choice to the choice it beats (used to determine the winner)
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_user_choice():
    """
    Ask the user to choose rock, paper, or scissors.
    Validates the input and keeps prompting until a valid choice is entered.
    Accepts shorthand inputs (r, p, s) for convenience.
    """
    shorthand = {"r": "rock", "p": "paper", "s": "scissors"}

    while True:
        user_input = input("Choose rock, paper, or scissors (r/p/s): ").strip().lower()

        # Allow single-letter shortcuts
        if user_input in shorthand:
            return shorthand[user_input]

        # Allow the full word
        if user_input in VALID_CHOICES:
            return user_input

        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors' (or r/p/s).\n")


def get_computer_choice():
    """
    Randomly select rock, paper, or scissors for the computer.
    """
    return random.choice(VALID_CHOICES)


def determine_winner(user_choice, computer_choice):
    """
    Compare the user's and computer's choices and determine the result.
    Returns one of: 'user', 'computer', or 'tie'.
    """
    if user_choice == computer_choice:
        return "tie"

    # If the user's choice beats the computer's choice, the user wins
    if BEATS[user_choice] == computer_choice:
        return "user"

    # Otherwise the computer wins
    return "computer"


def display_round_result(user_choice, computer_choice, result):
    """
    Print the choices made by both players and announce the round's outcome.
    """
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    if result == "tie":
        print("It's a tie!\n")
    elif result == "user":
        print("You win this round!\n")
    else:
        print("Computer wins this round!\n")


def get_yes_no(prompt):
    """
    Ask a yes/no question and validate the input.
    Returns True for 'y' / 'yes' and False for 'n' / 'no'.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Invalid input. Please answer with 'y' or 'n'.\n")


def display_final_score(user_score, computer_score, ties):
    """
    Print the final score summary and overall game result before exiting.
    """
    print("=" * 50)
    print("FINAL SCORE")
    print("=" * 50)
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")

    if user_score > computer_score:
        print("\nCongratulations, you won the game overall!")
    elif computer_score > user_score:
        print("\nThe computer won the game overall. Better luck next time!")
    else:
        print("\nThe overall game ended in a tie!")


def main():
    """
    Main game loop: plays rounds of Rock-Paper-Scissors, tracks the score
    across rounds, and asks whether to play again after each round.
    """
    print("=" * 50)
    print("      ROCK - PAPER - SCISSORS")
    print("=" * 50)
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

    # Running totals tracked across all rounds played in this session
    user_score = 0
    computer_score = 0
    ties = 0
    round_number = 1

    while True:
        print(f"--- Round {round_number} ---")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        display_round_result(user_choice, computer_choice, result)

        # Update the running score based on the round's result
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1

        # Show the current score after every round
        print(f"Score -> You: {user_score} | Computer: {computer_score} | Ties: {ties}\n")

        # Ask whether to play another round
        if not get_yes_no("Play another round? (y/n): "):
            break

        round_number += 1
        print()  # blank line for readability between rounds

    print()
    display_final_score(user_score, computer_score, ties)
    print("\nThanks for playing! Goodbye.")


# Standard Python entry point check
if __name__ == "__main__":
    main()
