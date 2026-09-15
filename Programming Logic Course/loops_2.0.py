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
       - Prints "[number] bottles of beer on the wall!... the full stanza, correcting to singualr for 1
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

"""
Assignment 4B: Loops
Date:9/10/26
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

bored_child = True

while bored_child:
    print("\nCan we sing a song?")

    answer = input("\nParents say: ").lower()

    bored_child = print("\nExcited child: Yay!\n")

    if answer == "yes":

        for n, m in zip(range(99, 1, -1), range(98, 0, -1)):
            if m > 1:
                print(
                    f"{n} bottles of beer on the wall, {n} bottles of beer. Take one down and pass it around, {m} bottles of beer on the wall."
                )
            elif m == 1:
                print(
                    f"{n} bottles of beer on the wall, {n} bottles of beer. Take one down and pass it around, {m} bottle of beer on the wall."
                )
        print(
            "1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall!."
        )
        print(
            "\nNo more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall!"
        )
        bored_child = print("\nHappy child: Again, again!")

print("\nParents: Ugh... absolutely not!\n")
