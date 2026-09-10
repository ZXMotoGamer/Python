"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

"""
Assignment 4B: Loops
Date:9/[ ]/26
File Name: Loops.py
"""

whiny = True

while whiny:
    print("\nAre we there yet?\n")

    answer = input("Parents say: ").lower()

    if answer == "yes":
        whiny = False

board = True

while board:
    print("\nCan we sing a song?")

    answer = input("\nParents say: ").lower()

    if answer == "yes":
        board = print(
            "99 bottles of beer on the wall, 99 bottles of beer. Take one down and pass it around, 98 bottles of beer on the wall."
        )
        for n in range(98, 1, -1):
            print(f"{n} bottles of beer on the wall, {n} bottles of beer.")

print(
    "1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall."
)

print("\nParents: Ugh...never again.")

# 99 bottles of beer on the wall, 99 bottles of beer
# Take one down and pass it around, 98 bottles of beer on the wall
