"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

"""
Assignment 5A: Input Validation
Date: 9/20/2026
File: registration.py
"""

# first name
# last name
# age - > 21 = drink added drink ticket
# phone number
# how many tickets

# additional tickets = EC

# ----------------------------------------------------------[Code Start]------------------------------------------------------------------------
while True:
    first_name = input("\nWhat's your first name? ").strip().capitalize()
    if first_name == "":
        print("\nSorry, that is not a valid name please try again.")
    else:
        break
while True:
    last_name = input("\nWhat's your last name? ").strip().capitalize()
    if last_name == "":
        print("\nSorry, that is not a valid name please try again.")
    else:
        break

# for the First and Last name inputs I used "IF/Else" statements inside of a "while" loop to ensure that a name was entered. I also used ".strip()" to make sure spaces were treated the same as no input at all. finally I used ".capitalize()" to well of course capitalize the first letters of the names.

while True:
    try:
        age = int(input("\nHow old are you? "))
        if age <= 0:
            print("\nSorry, that is not a valid age please try again.")
        elif age > 120:
            print("\nSorry, that is not a valid age please try again.")
        elif age < 21:
            alcohol = "Not eligible"
            break
        elif age > 20:
            alcohol = "Eligible"
            break
        else:
            break
    except ValueError:
        print("\nSorry, you must enter a numerical number please try again.")
        continue

# Age input is forced to have a numerical number entered via use of "try/except",this also stops any spaces or non-inputs to be accepted. Invalid inputs are rejected via "IF/Elif/Else" statements using comparison operators, along with alcoholic drinks being enabled for individuals ages 21 and onward, and also disabled for those under the age of 21. All reside in a "while" loop to make sure an input is entered.

while True:
    try:
        phone = int(input("\nEnter a reliable emergency phone number please. "))
        break
    except ValueError:
        print(
            "\nSorry that is not a valid phone number. Enter a numerical number, please do not include any spaces or dashes."
        )
        continue

# phone is handled the same way that age is with the exception of "IF/Elif/Else" statement that are not needed.

while True:
    try:
        tickets = int(input("\nHow many tickets do you need? "))
        if tickets > 999999999999999999999999999999999:
            print(
                "Sorry, that is too many ticket for one purchase. Please reduce the amount of tickets."
            )
            continue
        elif tickets > 0:
            break
        else:
            print(
                "\nTickets are required to entry. Please enter the number of tickets you need per person."
            )
            continue
    except ValueError:
        print("\nSorry, you must enter a numerical number please try again.")
        continue

# tickets uses all "IF/Elif/Else", "try/except", and a "while" loop to make sure an acceptable input is entered by the user.

entry_registration = "Entry Registration"

# "entry_registration is used for a title."

print(f"\n\n{entry_registration:>30}\n")
print(f"\nFirst Name:{first_name:>30}")
print(f"\nLast name:{last_name:>31}")
print(f"\nAge:{age:>37}")
print(f"\nAlcoholic drinks:{alcohol:>24}")
print(f"\nEmergency phone number:{phone:>18}")
print(f"\nTickets:{tickets:>33}\n")
print("\n\tThank you for registering.\n\n")

# the print statements above present the inputs entered to the user in a clean display.

# ----------------------------------------------------------[Code End]--------------------------------------------------------------------------
