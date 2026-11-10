# Master example 2
# Used for assignment 12A
# I guess this is suppose to be integrated into my final project.

import datetime
import os


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def read_menu():
    menus = {}
    try:
        with open("final_project_folder\\menu.txt", "r") as file:
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
    services = menu_items.get("SERVICES")
    oil_weight = menu_items.get("OIL WEIGHT")
    add_ons = menu_items.get("ADDITIONAL SERVICES")
    return services, oil_weight, add_ons


def print_menu():
    """This section deliberately incomplete"""
    clear_screen()
    print("Services\n")
    services_item = services.split(",")
    for item in services_item:
        print(f"\t{item.strip()}")

    clear_screen()
    print("Oil Weight\n")
    oil_weight_item = oil_weight.split(",")


def main():
    menu_items = read_menu()
    services, oil_weight, add_ons = split_into_variables(menu_items)
    print_menu(services, oil_weight, add_ons)


main()
