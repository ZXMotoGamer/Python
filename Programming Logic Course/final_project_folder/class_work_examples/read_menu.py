# Master example 2
# Used for assignment 12A
# I guess this is suppose to be integrated into my final project.

import datetime


def read_menu():
    menus = {}
    try:
        with open("final_project_folder//menu.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail
        return menus
    except Exception as e:
        right_now = datetime.datetime.now()
        with open("error_log.txt", "a") as file:
            file.write(f"{right_now}, e")
        print(e)


def split_into_variables(menu_items):
    SERVICES = menu_items.get("SERVICES")
    OIL_WEIGHT = menu_items.get("OIL WEIGHT")
    ADD_ONS = menu_items.get("ADDITIONAL SERVICES")
    return SERVICES, OIL_WEIGHT, ADD_ONS


def print_menu(coffee, prices, milks, flavors, shots):
    """This section deliberately incomplete"""
    print("Coffee\n")
    coffee_item = coffee.split(",")
    for item in coffee_item:
        print(f"\t{item.strip()}")


def main():
    menu_items = read_menu()
    coffee, prices, milks, flavors, shots = split_into_variables(menu_items)
    print_menu(coffee, prices, milks, flavors, shots)


main()
