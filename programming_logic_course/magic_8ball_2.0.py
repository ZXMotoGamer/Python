"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

"""
Assignment 7B: The Magic 8 Ball
Date: 10/08/2026
File: magic_8ball_2.0.py
"""

# TODO: Create a tuple of at least 8 responses
# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop

import random

print("\nWelcome to the Digital Oracle!")

RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Eww",
    "Sounds like a personal problem",
    "Too late",
    "Try rubbing a lamp",
    "I'd love to help, but I'm only a ball",
    "Hang in there",
    "Don't worry I'm right by your side",
    "I wouldn't",
    "I would",
    "True",
    "False",
    "Sounds good to me",
    "Give up",
    "Don't do it",
    "Do it",
    "I'm busy",
    "Are you serious?",
    "Sorry",
    "Why ask me",
    "Hello",
    "leave me alone",
)
# Above is the eight balls tuple of many different responses to the user.


while True:
    # Above, "WHILE TRUE" keeps the eight ball asking unless the user quits.
    try:
        # Above, "Try:Except" catches any possibly errors that may crash eight ball.
        question = (
            input('\nAsk me something! or type "Quit" to quit.\n\n').strip().lower()
        )
        # Above, "question" variable ask the user to ask something to the eight ball while cleaning the input by the user to ensure quitting the game is possible.

        # if "quit" in question:
        # print("\nGoodbye\n")
        # break

        #  Above, I was going to use the above "if" statement to search the users input in case they type "I want to quit", however if they ask a real question like "Should I quit my job" that would cause the game to end instead of the eight ball giving an answer.

        # if question == "quit":
        #     print("Goodbye")
        #     break
        # Above, "if" statement ends/quits the program if the correct input is entered by the user.

        if "quit" in question:  # **CORRECTED**
            print("\nGoodbye\n")
            break
        # Above, "if" statement ends/quits the program if "quit" is in the user input.
        elif not question:  # **CORRECTED**
            # I had forgotten that "not" is opposite variable value, and agree is a cleaner simpler way to code this "elif".
            print("\nThis isn't a game! Ask me something!\n\n")
            continue
        # Above, "elif" was for fun to ensure a question has been asked.
        else:
            answer = random.choice(RESPONSES)
            print(f"\nOracle: {answer}\n")
        # Above, "else" statement uses "random.choice" to pull a random output to display to the user from the eight balls tuple list.
    except Exception as e:
        print("\nUnexpected error, please try again.")
        continue
