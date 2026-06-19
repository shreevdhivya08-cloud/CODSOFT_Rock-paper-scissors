# Python Rock-Paper-Scissors Game

A beginner-friendly, command-line Rock-Paper-Scissors game. Play against the computer across as many rounds as you like, with running score tracking and a final summary at the end.

## Features

- Play Rock, Paper, or Scissors against a randomized computer opponent
- Accepts full words (`rock`, `paper`, `scissors`) or shorthand (`r`, `p`, `s`)
- Displays both the player's and the computer's choice each round
- Determines and announces the winner of each round
- Tracks score (wins, losses, and ties) across multiple rounds
- Replay any number of rounds without restarting the program
- Displays a final score summary and overall winner before exiting
- Handles invalid input gracefully with clear error messages
- Built using only Python's standard library (`random` module) — no external dependencies

## Requirements

- Python 3.6 or higher

No additional packages need to be installed.

## How to Run

1. Make sure Python 3 is installed on your system.
2. Download or copy `rock_paper_scissors.py` to your computer.
3. Open a terminal (or command prompt) and navigate to the folder containing the file.
4. Run the script:

   ```bash
   python3 rock_paper_scissors.py
   ```

   On Windows, you may need to use:

   ```bash
   python rock_paper_scissors.py
   ```

## Example Session

```
==================================================
      ROCK - PAPER - SCISSORS
==================================================
Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.

--- Round 1 ---
Choose rock, paper, or scissors (r/p/s): rock

You chose: Rock
Computer chose: Scissors
You win this round!

Score -> You: 1 | Computer: 0 | Ties: 0

Play another round? (y/n): y

--- Round 2 ---
Choose rock, paper, or scissors (r/p/s): p

You chose: Paper
Computer chose: Paper
It's a tie!

Score -> You: 1 | Computer: 0 | Ties: 1

Play another round? (y/n): n

==================================================
FINAL SCORE
==================================================
You: 1
Computer: 0
Ties: 1

Congratulations, you won the game overall!

Thanks for playing! Goodbye.
```

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Matching choices result in a tie

## How It Works

1. **User input** – The player is prompted to choose rock, paper, or scissors, using either the full word or a single-letter shortcut.
2. **Computer choice** – The computer randomly selects one of the three options using Python's `random.choice()`.
3. **Winner determination** – A lookup table (`BEATS`) maps each choice to the choice it defeats, allowing a simple, readable comparison to decide the round's outcome.
4. **Score tracking** – Wins, losses, and ties are tallied in variables that persist across rounds within the same session.
5. **Replay loop** – After each round, the player is asked whether to continue. The game keeps running until the player chooses to stop.
6. **Final summary** – Once the player decides to stop, the total score is displayed along with the overall winner of the session.

## Input Validation

The program handles invalid input gracefully and will re-prompt instead of crashing if:

- The player enters anything other than `rock`, `paper`, `scissors`, or their shorthand (`r`, `p`, `s`)
- A yes/no question receives anything other than `y`/`yes` or `n`/`no`

## Project Structure

```
rock_paper_scissors.py   # Main script with all logic and comments
README.md                 # This documentation file
```

## Possible Enhancements

- Add a "best of N rounds" mode
- Add Rock-Paper-Scissors-Lizard-Spock variant
- Track game statistics across sessions using a file or database

## License

This project is free to use, modify, and distribute for personal or educational purposes.
