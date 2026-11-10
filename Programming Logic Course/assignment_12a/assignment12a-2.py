"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

"""
Assignment: 12A-2
Date: //2026
File: assignment12a.py
"""
import datetime


def read_menu():
    menus = {}
    try:
        with open("menu_config.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail
        return menus
    except FileNotFoundError:
        print(
            'Please create the file or check the file name. It should be "menu_config.txt"'
        )
        return {}
    except IndexError:
        return menus
    except Exception as e:
        right_now = datetime.datetime.now()
        with open("error_log.txt", "a") as file:
            file.write(f"{right_now}, {e}\n")
        print(e)


def split_into_variables(menu_items):
    services = menu_items.get("SERVICES")
    oil_weights = menu_items.get("OIL WEIGHT")
    add_ons = menu_items.get("ADDITIONAL SERVICES")
    return services, oil_weights, add_ons


def print_services(services):
    print("Services\n")
    services_item = services.split(",")
    for item in services_item:
        print(f"\t{item.strip()}")


def print_oil_weights(oil_weights):
    print("\nOil weights\n")
    oil_weights_item = oil_weights.split(",")
    for item in oil_weights_item:
        print(f"\t{item.strip()}")


def print_add_ons(add_ons):
    print("\nAdditional services\n")
    add_ons_item = add_ons.split(",")
    for item in add_ons_item:
        print(f"\t{item.strip()}")


def main():
    menu_items = read_menu()
    services, oil_weights, add_ons = split_into_variables(menu_items)
    print_services(services)
    print_oil_weights(oil_weights)
    print_add_ons(add_ons)


main()
