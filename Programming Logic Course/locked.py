"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

"""
Assignment: 6B
Date: /  /
File: locked.py
"""

JAGEX = "Runescape"

USER_NAMES = (
    "Master_Meri",
    "Brent_the_Slayer",
    "Ghost_0100",
    "Weird_Al1",
    "Hendrix_is_bae",
)

passwords = ["DebugsTheDuck", "KratosAxe", "WillMoto4Ever", "DriveThru", "PurpleShorts"]

rs_account_settings = True

menu = "1. Look up username\n2. Change username\n3. Change password\n4. Quit"

print("\n\t\t\t⚔️   Top Runscape Players ⚔️\n")

print(USER_NAMES)

while rs_account_settings:
    try:
        print("\n\t\tSettings")
        print(f"\n{menu}")
        user_request = int(input("\nPlease enter an option: "))
    except ValueError:
        print("Please enter a number option.")
        continue

    match user_request:
        case 1:
            while True:
                user_search = input("\nSearch: ")
                if user_search not in USER_NAMES:
                    print("\nNo that is not a player, please try again.")
                    continue
                else:
                    print("\nYes that is a player")
                    break
        case 2:
            username_change = input("\nWhich username would you like to change? ")
            if username_change not in USER_NAMES:
                print("\nSorry that username does not exist, please try again.")
                continue
            else:
                print(f"\nCurrent Username: {username_change}")
                new_username = input("\nPlease enter new username: ")
                print(f"New username: {USER_NAMES[0]}")
