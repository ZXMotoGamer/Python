"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [9/7/2026]
FILE: buffet.py
-----------------------------------------------------------------------
-----------------------------------------------------------------------
"""

"""
ASSIGNMENT: 3B - Updated
DATE: [9/8/2026]
"""

user_day = input("\nWhat day is it? ").lower()
# I wrote this line to ask the user what day they required information about.
# I also converted the input to lower case in order to feed the match/case compiler.


match user_day:
    case "tuesday":
        child_price_per_year = 0.50
    case "sunday":
        child_price_per_year = 1.00
        print("\nFree Drinks!")
    case _:
        child_price_per_year = 1.00
# I used match case to pin certain price rules for children to certain days of the week.
# I also pinned any specials to certain days as well.


age = int(input("\nWhat is you're age? "))


if age < 1:
    print(f"\nDay: {user_day}\t\tAge: {age}\t\tPrice: $0.00 Free of Charge!\n")
elif age < 13:
    print(
        f"\nDay: {user_day}\t\tAge: {age}\t\tPrice: ${child_price_per_year * age:.2f}\n"
    )
elif age < 65:
    print(f"\nDay: {user_day}\t\tAge: {age}\t\tPrice: $16.95\n")
else:
    print(f"\nDay: {user_day}\t\tAge: {age}\t\tPrice: $12.95\n")
# I used if/elif/else statements along with f-strings to determine what day, what age, and what price data is needed to answer inputs provided.


# *** I updated my if/elif/else statements along with my comments for this assignment. ***
