"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, price) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

"""
Assignment: 9A
Date: 10/19/2026
File: smoothie_bar.py
"""


# GLOBAL CONSTANTS (The Pantry)
SIZES = ("Small", "Medium", "Large")
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")
# Above, are global "tuples" for the program to display to the user for item selection.


# TODO: Define get_price(size)
def get_price(size):
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 5.00
    elif size == "Large":
        return 7.00
    else:
        print("\nSorry, that is not a size. Would you like a small, medium, or large?.")
        return 0.00


# Above, is a "function" called "def get_price(size)" it assigns pricing for the different sizes that are available to the user to choose.


# TODO: Define blend(size, base, fruit, price)
def blend(size, base, fruit, scoops, price):
    print("\n\tSmoothie Bar Invoice\n")
    print(f"Size:{size:>32}")
    print(f"Base:{base:>32}")
    print(f"Fruit:{fruit:>31}")
    print(f"Scoops:{scoops:>30}")
    print(f"Price:{f'${price:.2f}':>31}")
    print("\n\tEnjoy your smoothie!")
    print("\tThank you!\n")


# Above, is a "function" called "def blend(size, base, fruit, scoops, price)" it displays the invoice to the user of the entire order they entered into the program.


# TODO: Define main() to collect input and call your logic
def main():  # "def main()" is what has the base code of the program and uses two "functions" above to do certain tasks.
    print("\nHello! welcome to the smoothie bar!")
    while True:
        try:
            print(f"\n{SIZES}")
            user_size = input("\nWhat size would you like?  ").strip().capitalize()
            price = get_price(user_size)
            if price > 0:
                break
            else:
                continue
        except Exception as e:
            print(f"\nUnexpected Error {e} occurred, please try again.")
            continue
    # Above, The "while True" asks the user for what size they would like. The "input" is cleaned up to meet the needs of the "get_price(size)" "function" via ".strip()" to remove spaces and ".capitalize()" to capitalize the first letters of the users entry. Within the loop the "get_price()" "function" assigns the correct price to the size that the user has requested. The loop uses an "if/else" statement to make sure that a valid size is entered by the user. A "try:except" blocks any unexpected errors there may be.

    while True:
        try:
            print(f"\n{BASES}")
            user_base = (
                input("\nWhat base would you like for your smoothie? ").strip().title()
            )
            if user_base not in BASES:
                print(f"\nSorry, that is not available, please choose from the menu.")
                continue
            else:
                break
        except Exception as e:
            print(f"\nUnexpected error: {e} has occurred. Please try again.")
    # Above, this "while True" asks the user what base they would like for their smoothie. ".strip()" and ".title()" clean up the input to ensure that the entry by the user is correct compared to the "tuple". It uses the "in" operator to check if the users input is in the "BASES" "tuple". Finally an "if/else" statement is used to determine if the input is valid or not.

    while True:
        try:
            print(f"\n{FRUITS}")
            user_fruit = (
                input("\nWhat fruit would you like for your smoothie?  ")
                .strip()
                .capitalize()
            )
            if user_fruit not in FRUITS:
                print("\nSorry, that is not available, please choose from the menu.")
                continue
            else:
                break
        except Exception as e:
            print(f"\nUnexpected error: {e} has occurred. Please try again.")
    # Above, is another "while True" loop for the "FRUITS" "tuple" it is handled in the same manor as the "BASES" "tuple" before it.

    while True:
        try:
            user_scoops = int(
                input("\nHow many scoops would you like for your smoothie?  ")
            )
            if user_scoops <= 0:
                print("\nYou need at least 1 scoop to get a smoothie.")
                continue
            elif user_scoops > 4:
                print("\nSorry, no more than 4 scoops per-smoothie.")
                continue
            else:
                break
        except ValueError:
            print(
                "\nPlease enter the numerical number of scoops you would like in your smoothie."
            )
        except Exception as e:
            print(f"\nUnexpected error: {e} has occurred. Please try again.")
    # Above, is a "while True" that asks the user how many scoops they would like in their smoothie. It uses an "if/elif/else" statement to make sure only the allowed number of scoops is accepted. The input is also kept in check with the "try:except" block that rejects any non numerical inputs by the user.

    blend(user_size, user_base, user_fruit, user_scoops, price)
    # Above, "blend()" "function" puts all the inputs from the user for their order together in a neat clean presentation.


main()
