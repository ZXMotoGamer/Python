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
Date: 10//2026
File: pizza_engine.py
"""
MENU = "\n1. Order pizza\n2. Quit"
PIZZA_SIZES = (10, 14, 18, 20)
PIZZA_DOUGHS = ("Thin", "Double", "Deep Dish")
PIZZA_CHEESE = ("Light", "Regular", "Extra")
MEAT_TOPPINGS = ("Peperoni", "Sausage", "Bacon", "Ground Beef", "Ham", "Italian Beef")
VEGGIE_TOPPINGS = ("Green pepper", "Mushroom", "Onion", "Tomatoes", "Spinach")


def make_pizza(
    name,
    size="14",
    dough="Thin",
    cheese="Regular",
    meat="None",
    veggies="None",
    delivery=False,
):

    print("\t\tCustomer Order\n")
    print(f"Customer Name: {name}")
    print(f"Size: {size}")
    print(f"Dough: {dough}")
    print(f"Cheese: {cheese}")
    print(f"Meat: {meat}")
    print(f"Veggies: {veggies}")
    print(f"Delivery: ")
    print("\nEnjoy your pizza!")
    print("Thank you! Come again!")
    pass


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
                    except ValueError:
                        print("\nInvalid entry, please enter a numerical number.")
                        if pizza_size in PIZZA_SIZES:
                            break
                        else:
                            option_not_available()
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
                    meat_topping = input("\nEnter your meat topping: ").strip().title()
                    if meat_topping not in MEAT_TOPPINGS:
                        option_not_available()
                    else:
                        break
                while True:
                    print(f"\n{VEGGIE_TOPPINGS}")
                    veggie_topping = (
                        input("Enter your veggie topping: ").strip().title()
                    )
                    if veggie_topping not in VEGGIE_TOPPINGS:
                        option_not_available()
                        continue
                    else:
                        break
                while True:
                    order_type = (
                        input("\nIs this for delivery or pickup: ").strip().lower()
                    )
                    if order_type == "delivery":
                        delivery = True
                    elif order_type == "pickup":
                        break
                    else:
                        print("\nSorry option not available.")
                        continue
                make_pizza(
                    user_name,
                    pizza_size,
                    pizza_dough,
                    pizza_cheese,
                    meat_topping,
                    veggie_topping,
                    order_type,
                )
                break
            case 2:
                print("\nGoodbye\n")
                break
            case _:
                print("\nPlease enter one of the menu options.\n")
                continue


main()
