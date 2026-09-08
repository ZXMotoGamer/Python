price = float(input("cost of pie? "))
print(f"pie is {price:>20.2f}")
# print(f"pie is                                   ${price:.2f}")
# print(f"pie is ................................. ${price:.2f}")
# can the $ symbol be attached to the price variable so that is is printed in front of it without using spaces or dots.


user_day = input("\nWhat day is it? ").lower()

match user_day:
    case "tuesday":
        child_price_per_year = 0.50
    case "sunday":
        child_price_per_year = 1.00
        print("\nFree Drinks!")
    case _:
        child_price_per_year = 1.00

age = int(input("\nWhat is you're age? "))


if age < 1:
    print(f"\nDay:{user_day}\t\tAge:{age}\t\tPrice:$0.00 Free of Charge!\n")
elif age < 13:
    print(f"\nDay:{user_day}\t\tAge:{age}\t\tPrice:${child_price_per_year * age:.2f}\n")
elif age < 65:
    print(f"\nDay:{user_day}\t\tAge:{age}\t\tPrice:$16.95\n")
elif age > 64:
    print(f"\nDay:{user_day}\t\tAge:{age}\t\tPrice:$12.95\n")


# how do I have "Free Drinks" print after the (if/elif) function but also attached to only appear for the (match) day of sunday?
# is this even necessary?
# should I care?
