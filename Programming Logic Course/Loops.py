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
print("\nThe Child...")

whiny_child = True

while whiny_child:
    print("\nAre we there yet?\n")

    answer = input("Parents say: ").lower()

    if answer == "yes":
        whiny_child = False
# I made a whiny child perform a "WHILE LOOP" asking if they are at their destination yet. This loop wont stop until the parents give in and say yes.

board_child = True

while board_child:
    print("\nCan we sing a song?")

    answer = input("\nParents say: ").lower()

    if answer == "yes":
        board_child = print(
            "\n99 bottles of beer on the wall, 99 bottles of beer. Take one down and pass it around, 98 bottles of beer on the wall."
        )
        for n, m in zip(range(98, 2, -1), range(97, 1, -1)):
            print(
                f"{n} bottles of beer on the wall, {n} bottles of beer. Take one down and pass it around, {m} bottles of beer on the wall."
            )
# After the parents give in the child becomes board and wants to sing a song and the "BOARD_CHILD" loop wont stop until the parents say yes as well.
# We all hate this song and so I wanted the whole song. In this "FOR" loop I wanted both numbers to count down but didn't know how to code it.
# I looked up if there was a function to combine two countdown ranges in a single line and learned about the "ZIP()" function.
# At first I could not get it to work because once again I thought and wrote as a human would. I figured out again you have to be very detailed and code both ranges with all the info for both "FOR" variables.
# This was cool and I got a kick out of finding out how to combined the ranges so that both numbers would countdown independently.

print(
    "2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall."
)
print(
    "1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall."
)
print(
    "\nNo more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall!."
)
# Had to adjust some words above for the last few lines of the song by manually printing them.

print("\nHappy Child: Again, again!")
print("\nParents: Ugh... absolutely not!\n")

# This was fun!
