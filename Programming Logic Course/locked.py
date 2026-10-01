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
Date: 9/30/2026
Time: 12:10am
File: locked.py
"""

JAGEX = "Runescape"
# Above is a Department constant/Title defined in ALL_CAPS.

USER_NAMES = (
    "Master_Meri",
    "Brent_the_Slayer",
    "Ghost_0100",
    "Weird_Al1",
    "Hendrix_is_bae",
)
# Above is a "tuple" list of usernames defined in ALL_CAPS to ensure it is not to be changed.

passwords = ["DebugsTheDuck", "KratosAxe", "WillMoto4Ever", "DriveThru", "PurpleShorts"]
# Above is a "list" or password that run parallel to the tuple of usernames.

rs_system_settings = True
# Above is a flag for the program to continue running until the value is changed.

login_menu = "\n1. CEO\n2. IT\n3. Sales\n4. Quit"
it_menu = "1. Search username\n2. Add username\n3. Change password\n4. Quit"
employee_menu = "1. Search username\n2. Username change\n3. Change password\n4. Quit"
# Above are three menus used by the program to display to the user for navigation of tasks the program performs.
# "login_menu" is to make sure that the correct following menu is displayed for the correct user.
# The "it_menu" and the "employee_menu" displays the correct options available to to the correct user.

while rs_system_settings:
    try:  # This "try" and its corresponding "except" block is used to catch a possible "ValueError" for the menu below. There are other "ValueError" blocks for the other two menus in this program.

        print(f"\n\t\t{JAGEX}")
        print(f"{login_menu}")
        employee_login = int(input("\nEnter job position: "))
        # Above is a menu for the user to input/login as their job position. This decides which following menu will be displayed next for the user.

        # Below is the main "Match:case" to display the correct menu based on the input entered into the "login_menu".
        # Each "case" of the main "match:case" is an option of the previous "login_menu"
        match employee_login:
            case 1:
                try:
                    while True:
                        print(f"\n\t\t{JAGEX}")
                        print("\nLogged in as: CEO")
                        print(f"\n{employee_menu}")
                        employee_request = int(input("\nSelect a menu option: "))
                        match employee_request:
                            case 1:
                                try:
                                    while True:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu')
                                        user_search = input("\nSearch: ")
                                        if (
                                            user_search == "Exit"
                                            or user_search == "exit"
                                        ):  # This "if" is used through out the program menus to allow the user to go mack to the menu after entering an option.
                                            break
                                        elif (
                                            user_search not in USER_NAMES
                                        ):  # This "elif" uses "not in" to let the user know if a username is not in the "tuple" list. It rejects the invalid input and asks the user to try again.
                                            print(
                                                "\nUsername does not exist, please try again."
                                            )
                                            continue
                                        else:  # "else" takes the input from the user and uses ".index()" to display the correct username ans parallel password that goes together.
                                            user_index = USER_NAMES.index(user_search)
                                            print(
                                                f"\nUsername: {user_search}\nPassword: {passwords[user_index]}"
                                            )
                                            break
                                except (
                                    IndexError
                                ):  # "IndexError" block helps to handle any unexpected errors with the ".index()" function being performed. This also happens throughout the program in other menus.
                                    print(
                                        "\nUnexpected error has occurred, please try again."
                                    )
                                    continue
                                except (
                                    Exception
                                ) as e:  # "Exception" block is to catch any errors that may crash the program that are not immediately apparent.
                                    print(
                                        f"\nUnexpected error {e} has occurred, please try again."
                                    )
                                    continue
                            case 2:
                                while True:
                                    try:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu')
                                        user_change = input(
                                            "\nEnter current username: "
                                        )
                                        if (
                                            user_change == "Exit"
                                            or user_change == "exit"
                                        ):
                                            break
                                        elif user_change not in USER_NAMES:
                                            print(
                                                "\nUsername does not exist, please try again."
                                            )
                                            continue
                                        else:  # "else" takes the users input and attempts tp change the username via converting the selected username residing in the "tuple" to a "list", modifying it and then converting it back into a "tuple" again.
                                            new_username = input(
                                                "\nEnter new username: "
                                            )
                                            user_index = USER_NAMES.index(user_change)
                                            USER_NAMES[user_index] = new_username
                                            break
                                    except (
                                        TypeError
                                    ):  # However this "TypeError" block catches the attempted change because the current user is not authorized to make the change.
                                        print(
                                            "\nError: Contact IT help desk via E-mail, a username change request has been sent."
                                        )
                                        break
                                    except Exception as e:
                                        print(
                                            f"\nUnexpected error {e} has occurred, please try again."
                                        )
                            case 3:
                                try:
                                    while True:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu')
                                        user_pass_change = input(
                                            "\nEnter username to change password: "
                                        )
                                        if (
                                            user_pass_change == "Exit"
                                            or user_pass_change == "exit"
                                        ):
                                            break
                                        elif user_pass_change not in USER_NAMES:
                                            print(
                                                "\nUsername does not exist, please try again."
                                            )
                                            continue
                                        else:  # "else" is taking the users input and changing the password, it does this by finding the ".index()" of the username input by the user and changing the parallel password that goes with it.
                                            user_index = USER_NAMES.index(
                                                user_pass_change
                                            )
                                            new_password = input(
                                                "\nEnter new password: "
                                            )
                                            passwords[user_index] = new_password
                                            print("\nPassword updated!")
                                            break
                                except IndexError:
                                    print(
                                        "\nUnexpected error has occurred, please try again."
                                    )
                                except Exception as e:
                                    print(
                                        f"\nUnexpected error {e} has occurred, please try again."
                                    )
                            case 4:
                                print("\nlogging out.")
                                break
                            case _:
                                print("\nPlease enter a number 1-4.")
                                continue
                except ValueError:
                    print("\nPlease enter a menu option number.")
            case (
                2
            ):  # "case 2:" has one difference in its menu which is to add a user. since this menu is meant for the IT employees they alone are allowed to change/ass usernames.
                try:
                    while True:
                        print(f"\n\t\t{JAGEX}")
                        print("\nLogged in as: IT")
                        print(f"\n{it_menu}")
                        user_request = int(input("\nSelect a menu option: "))
                        match user_request:
                            case 1:
                                try:
                                    while True:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu')
                                        user_search = input("\nSearch: ")
                                        if (
                                            user_search == "Exit"
                                            or user_search == "exit"
                                        ):
                                            break
                                        elif user_search not in USER_NAMES:
                                            print(
                                                "\nUsername does not exist, please try again."
                                            )
                                            continue
                                        else:
                                            user_index = USER_NAMES.index(user_search)
                                            print(
                                                f"\nUsername: {user_search}\nPassword: {passwords[user_index]}"
                                            )
                                            break
                                except IndexError:
                                    print(
                                        "\nUnexpected error has occurred, please try again."
                                    )
                                    continue
                                except Exception as e:
                                    print(
                                        f"\nUnexpected error {e} has occurred, please try again."
                                    )
                                    continue
                            case 2:
                                while True:
                                    try:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu')
                                        add_user = input("\nEnter new username: ")
                                        if add_user == "Exit" or add_user == "exit":
                                            break
                                        else:  # Here we have the IT employee able to add a user and modify the "tuple" unlike other unauthorized employees. IT does this by converting the Tuple into a list like the "user_change" however due to the fact that the user is logged in as an IT employee the adding and modification of the "tuple" list is successful.
                                            temp_list = list(USER_NAMES)
                                            temp_list.append(add_user)
                                            modded_USER_NAMES = tuple(temp_list)
                                            USER_NAMES = modded_USER_NAMES
                                            new_user_password = input(
                                                "\nCreate a password: "
                                            )  # Do to the fact a new user is being added a password must be created so the ".append()" function does this by adding the new password to the end of the list which matches up parallel to the new username added to the "tuple" vis converting it to a normal list, modifying it, and then converting it back to a "tuple".
                                            passwords.append(new_user_password)
                                            print(
                                                f"\nAdded new user account:\nUsername: {add_user}\nPassword: {new_user_password}"
                                            )
                                            break
                                    except Exception as e:
                                        print(
                                            f"\nUnexpected error {e} has occurred, please try again."
                                        )
                                        continue
                            case 3:
                                try:
                                    while True:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu')
                                        user_pass_change = input(
                                            "\nEnter username to change password: "
                                        )
                                        if (
                                            user_pass_change == "Exit"
                                            or user_pass_change == "exit"
                                        ):
                                            break
                                        elif user_pass_change not in USER_NAMES:
                                            print(
                                                "\nUsername does not exist, please try again."
                                            )
                                            continue
                                        else:
                                            user_index = USER_NAMES.index(
                                                user_pass_change
                                            )
                                            new_password = input(
                                                "\nEnter new password: "
                                            )
                                            passwords[user_index] = new_password
                                            print("\nPassword updated!")
                                            break
                                except IndexError:
                                    print(
                                        "\nUnexpected error has occurred, please try again."
                                    )
                                except Exception as e:
                                    print(
                                        f"\nUnexpected error {e} has occurred, please try again."
                                    )
                            case 4:
                                break
                            case _:
                                print("\nPlease enter a number 1-4.")
                                continue
                except ValueError:
                    print("\nPlease enter a menu option number.")
            case (
                3
            ):  # "case 3:" has the exact same menu and options and functions as "case 1:"
                try:
                    while True:
                        print(f"\n\t\t{JAGEX}")
                        print("\nLogged in as: Sales")
                        print(f"\n{employee_menu}")
                        employee_request = int(input("\nSelect a menu option: "))
                        match employee_request:
                            case 1:
                                try:
                                    while True:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu')
                                        user_search = input("\nSearch: ")
                                        if (
                                            user_search == "Exit"
                                            or user_search == "exit"
                                        ):
                                            break
                                        elif user_search not in USER_NAMES:
                                            print(
                                                "\nUsername does not exist, please try again."
                                            )
                                            continue
                                        else:
                                            user_index = USER_NAMES.index(user_search)
                                            print(
                                                f"\nUsername: {user_search}\nPassword: {passwords[user_index]}"
                                            )
                                            break
                                except IndexError:
                                    print(
                                        "\nUnexpected error has occurred, please try again."
                                    )
                                    continue
                                except Exception as e:
                                    print(
                                        f"\nUnexpected error {e} has occurred, please try again."
                                    )
                                    continue
                            case 2:
                                while True:
                                    try:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu.')
                                        user_change = input(
                                            "\nEnter current username: "
                                        )
                                        if (
                                            user_change == "Exit"
                                            or user_change == "exit"
                                        ):
                                            break
                                        elif user_change not in USER_NAMES:
                                            print(
                                                "\nUsername does not exist, please try again."
                                            )
                                            continue
                                        else:
                                            new_username = input(
                                                "\nEnter new username: "
                                            )
                                            user_index = USER_NAMES.index(user_change)
                                            USER_NAMES[user_index] = new_username
                                            break
                                    except TypeError:
                                        print(
                                            "\nContact IT help desk via E-mail, a username change request has been sent."
                                        )
                                        break
                                    except Exception as e:
                                        print(
                                            f"\nUnexpected error {e} has occurred, please try again."
                                        )
                            case 3:
                                try:
                                    while True:
                                        print(
                                            f"\n\t\t\t⚔️   Top Runscape Players ⚔️\n{USER_NAMES}"
                                        )
                                        print('\nEnter "Exit" to go back to menu')
                                        user_pass_change = input(
                                            "\nEnter username to change password: "
                                        )
                                        if (
                                            user_pass_change == "Exit"
                                            or user_pass_change == "exit"
                                        ):
                                            break
                                        elif user_pass_change not in USER_NAMES:
                                            print(
                                                "\nUsername does not exist, please try again."
                                            )
                                            continue
                                        else:
                                            user_index = USER_NAMES.index(
                                                user_pass_change
                                            )
                                            new_password = input(
                                                "\nEnter new password: "
                                            )
                                            passwords[user_index] = new_password
                                            print("\nPassword updated!")
                                            break
                                except IndexError:
                                    print(
                                        "\nUnexpected error has occurred, please try again."
                                    )
                                except Exception as e:
                                    print(
                                        f"\nUnexpected error {e} has occurred, please try again."
                                    )
                            case 4:
                                break
                            case _:
                                print("\nPlease enter a number 1-4.")
                                continue
                except ValueError:
                    print("\nPlease enter a menu option number.")
            case (
                4
            ):  # "case 4:" is meant to quit the program via the main menu by rendering "rs_system_settings" as "False"
                print("\nGoodbye!")
                rs_system_settings = False
            case (
                _
            ):  # This "case" is to catch any input to the main menu that is an invalid option that could crash the program.
                print("\nPlease enter a number 1-4.")
                continue
    except ValueError:
        print("\nPlease enter a menu option number.")
        continue
