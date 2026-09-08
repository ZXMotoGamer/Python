"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

"""
Assignment 4A: Boolean Logic (And/Or/Not)
Date: 9/8/26
File: The Logic Gate
"""

number_1 = int(input("\nPlease choose a number: "))
number_2 = int(input("\nOne more number if you wouldn't mind: "))


if number_1 > 0 and number_2 > 0:
    print("Both numbers are larger than 0")
else:
    print("One or both numbers is smaller than 0")

if number_1 > 100 and number_2 > 100:
    print("Both numbers are larger than 100")
else:
    print("One or both numbers are smaller than 100")

if number_1 % 2 == 0 or number_2 % 2 == 0:
    print("At least one number is even")
else:
    print("One or both numbers are odd")

if number_1 < 100 or number_2 < 100:
    print("One or both numbers are smaller then 100")
else:
    print("one or both numbers are larger than 100")

if number_1 != number_2:
    print("These numbers do not match")
else:
    print("These numbers match")

if not number_1 == 0:
    print("You're first number is not 0")
else:
    print("You're first number is 0")

if not number_2 == 0:
    print("You're second number in not 0")
else:
    print("You're second number is 0")
