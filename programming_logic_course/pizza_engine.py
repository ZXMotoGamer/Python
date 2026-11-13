"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

"""
Assignment: 10A
Date: 10/26/2026
File: pizza_engine.py
"""
MENU = "\n1. Order pizza\n2. Quit"
PIZZA_SIZES = (10, 14, 18, 20)
PIZZA_DOUGHS = ("Thin", "Double", "Deep Dish")
PIZZA_CHEESE = ("Light", "Regular", "Extra")
MEAT_TOPPINGS = (
    "Peperoni",
    "Sausage",
    "Bacon",
    "Ground beef",
    "Ham",
    "Italian beef",
    "None",
)
VEGGIE_TOPPINGS = ("Green pepper", "Mushroom", "Onion", "Tomatoes", "Spinach", "None")


def make_pizza(
    name,
    size="14",
    dough="Thin",
    cheese="Regular",
    meats="None",
    veggies="None",
    is_delivery=False,
):

    print("\t\tCustomer Order\n")
    print(f"Customer Name: {name}")
    print(f"Size: {size}")
    print(f"Dough: {dough}")
    print(f"Cheese: {cheese}")
    print(f"Meat: {meats}")
    print(f"Veggies: {veggies}")
    if is_delivery == False:
        print("Delivery: No")
    else:
        print("Delivery: Yes")
    print("\nEnjoy your pizza!")
    print("Thank you! Come again!\n")


def option_not_available():
    print("\nOption not available, please choose from the menu.")


def main():
    while True:
        print("\t\tWelcome to Pizza Planet!\n")
        print(MENU)
        try:
            user_menu = int(input("\nPlease enter a menu option: "))
        except ValueError:
            print("\nSorry, invalid menu option. Please enter a numerical option.\n")
            continue
        match user_menu:
            case 1:
                while True:
                    user_name = input("\nName for order: ").strip().title()
                    if not user_name:
                        print("\nA name is required to place an order.")
                        continue
                    elif user_name.isdigit():
                        print("\nPlease enter a valid name.")
                        continue
                    else:
                        break
                while True:
                    try:
                        print(f"\n{PIZZA_SIZES}")
                        pizza_size = int(input("\nEnter a size for your pizza: "))
                        if pizza_size not in PIZZA_SIZES:
                            option_not_available()
                            continue
                        else:
                            break
                    except ValueError:
                        print("\nInvalid entry, please enter a numerical number.")
                        continue
                while True:
                    print(f"\n{PIZZA_DOUGHS}")
                    pizza_dough = input("\nEnter your pizza dough: ").strip().title()
                    if pizza_dough not in PIZZA_DOUGHS:
                        option_not_available()
                        continue
                    else:
                        break
                while True:
                    print(f"\n{PIZZA_CHEESE}")
                    pizza_cheese = input("\nEnter your cheese amount: ").strip().title()
                    if pizza_cheese not in PIZZA_CHEESE:
                        option_not_available()
                    else:
                        break
                while True:
                    print(f"\n{MEAT_TOPPINGS}")
                    meat_topping = (
                        input("\nEnter your meat topping: ").strip().capitalize()
                    )
                    if meat_topping not in MEAT_TOPPINGS:
                        option_not_available()
                    else:
                        break
                while True:
                    print(f"\n{VEGGIE_TOPPINGS}")
                    veggie_topping = (
                        input("\nEnter your veggie topping: ").strip().capitalize()
                    )
                    if veggie_topping not in VEGGIE_TOPPINGS:
                        option_not_available()
                        continue
                    else:
                        break
                while True:
                    user_order_type = input("\nIs this for delivery: ").strip().lower()
                    if user_order_type == "yes":
                        delivery = True
                        break
                    elif user_order_type == "no":
                        delivery = False
                        break
                    else:
                        print('\nSorry, please enter "Yes" or "No"')
                        continue
                make_pizza(
                    name=user_name,
                    size=pizza_size,
                    dough=pizza_dough,
                    cheese=pizza_cheese,
                    meats=meat_topping,
                    veggies=veggie_topping,
                    is_delivery=delivery,
                )
                break
            case 2:
                print("\nGoodbye\n")
                break
            case _:
                print("\nPlease enter one of the menu options.\n")
                continue


main()
