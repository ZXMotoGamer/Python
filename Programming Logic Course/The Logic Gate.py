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
Date: 9/9/26
File: The Logic Gate
"""

number_1 = int(input("\nPlease choose a number: "))
number_2 = int(input("\nOne more number if you wouldn't mind:  "))
# I made simple variables for two numbered inputs.

print("\nResults:")
# this is a title for the following output information.

if number_1 > 0 and number_2 > 0:
    print("\nBoth numbers are equal to or larger than 0.")
# elif number_1 == 0 and number_2 == 0:
# print("\nBoth numbers are 0.")
else:
    print("\nOne or both numbers are equal to or smaller than 0.")

# I originally wrote and "ELIF" if the inputs equaled 0 due to the fact that 0 is not greater or less than 0. However, I decided it was unnecessary additional code and updated the "IF" and "ELSE" outputs for this and the following information.
# I learned that I could "PASS" statements so that no output would be given. I was going to go this route for the "ELIF" if both inputs were 0 but I didn't want to exclude any outputs from the assignment.

if number_1 > 100 and number_2 > 100:
    print("\nBoth numbers are equal to or larger than 100.")
else:
    print("\nOne or both numbers are equal to or smaller than 100.")

if number_1 % 2 == 0 or number_2 % 2 == 0:
    print("\nOne or both numbers are even.")
else:
    print("\nBoth numbers are odd.")

if number_1 < 100 or number_2 < 100:
    print("\nOne or both numbers are equal to or smaller then 100.")
else:
    print("\nOne or both numbers are equal to or larger than 100.")

if not number_1 == number_2:
    print("\nThese numbers do not match.")
else:
    print("\nThese numbers match.")

if not number_1 == 0:
    print("\nYou're first number is not 0.")
else:
    print("\nYou're first number is 0.")

# I would have combined "NOT" number_1 and "NOT" number_2 with "AND" but the assignment doesn't specify "Both Not Zero"

if not number_2 == 0:
    print("\nYou're second number is not 0.")
else:
    print("\nYou're second number is 0.")

if number_1 < 0:
    print(f"\n{number_1} is a negative number.\n")
elif number_1 > 0:
    print(f"\n{number_1} is a positive number.\n")
else:
    print("\nYou're first number is 0.\n")

# I used comparison operators with logic operators throughout the coding above. I could have done less repetitive coding but wanted to show all the logic checks for the assignment.
