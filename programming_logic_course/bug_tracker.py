"""
Assignment: 11A
Date: 11/2/2026
File: bug_tracker.py
"""

import datetime

# Imported "datetime" in order to be able to make a time stamp for logging files.

BUG_LOG_MENU = "\n\t\tBug Tracker\n\n1. Log a bug\n2. Quit\n"
# Above, is a menu to be displayed to the user for system navigation.


def make_bug_log():
    while True:
        file = input("\nEnter file name: ").strip().upper()
        if not file:
            print("File name is required to log bug.")
        else:
            break
    while True:
        description = input("\nEnter bug details: ").strip().upper()
        if not description:
            print("Description is required for bug log.")
        else:
            break
    PRIORITY_LEVEL_OPTIONS = ("LOW", "MEDIUM", "HIGH")
    while True:
        priority_level = input("\nEnter priority level: ").strip().upper()
        if priority_level not in PRIORITY_LEVEL_OPTIONS:
            print(
                "\nPlease enter a valid priority level for this bug log.\nExample: LOW, MEDIUM, HIGH."
            )
        else:
            break
    timestamp = datetime.datetime.now()
    bug_details = (
        f"File: {file}\nDescription: {description}\nPriority: {priority_level}"
    )
    with open("bug_log.txt", "a") as log_file:
        log_file.write(f"\n{timestamp}\n{bug_details}\n")


# Above, "make_bug_log()" function displays prompts for the user to log information. It uses "while loops" to continue running until valid data is entered. "if/else" statements are used to reject invalid inputs that are not allowed. The variable "timestamp" captures the date and time right after the user enters the bug information. Another variable "bug_details" takes the inputs from the user and combines them as well as sets them up to be written cleanly. Finally, both "timestamp" and "bug_details" get written to a text file that with add new bug entry logs.


def main():
    while True:
        try:
            print(BUG_LOG_MENU)
            bl_menu_choice = int(input("\nEnter a menu option: "))
            match bl_menu_choice:
                case 1:
                    make_bug_log()
                case 2:
                    print("\nGoodbye\n")
                    break
                case _:
                    print("\nNot a valid option, please try again.")
                    continue
        except ValueError:
            print("\nPlease enter a numerical number from the displayed menu.")
            continue
        except Exception as e:
            print(e)
            continue


# Above, "main()" function controls how the program run by controlling what order tasks/functions are performed.

main()
