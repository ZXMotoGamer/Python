"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [9/7/2026]
FILE: buffet.py
-----------------------------------------------------------------------
-----------------------------------------------------------------------
"""

user_day = input("\nWhat day is it? ").lower()

match user_day:
    case "tuesday":
        child_price_per_year = 0.50
    case "sunday":
        child_price_per_year = 1.00
        print("\nFree Drinks!")
    case _:
        child_price_per_year = 1.00
# tuesdays child price is set to what the business requested.
# sundays "Free Drinks" notice has been set as the business requested.
# all days of the week other than tuesday has been set to the normal child price as the business requested.

age = int(input("\nWhat is you're age? "))


if age < 1:
    print(f"\nDay:{user_day}\t\tAge:{age}\t\tPrice:$0.00 Free of Charge!\n")
elif age < 13:
    print(f"\nDay:{user_day}\t\tAge:{age}\t\tPrice:${child_price_per_year * age:.2f}\n")
elif age < 65:
    print(f"\nDay:{user_day}\t\tAge:{age}\t\tPrice:$16.95\n")
elif age > 64:
    print(f"\nDay:{user_day}\t\tAge:{age}\t\tPrice:$12.95\n")

# the prices have been set to their decided ages as the business requested.
