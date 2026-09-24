"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a loop (using a state flag or while True) to remain awake.
[ ] 3. Main menu uses match-case logic with a wildcard (case _) for selections.
[ ] 4. Inputs are validated using try-except blocks to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

"""
Assignment 5B: The ATM Boss
Date: 9/23/26 
File name: atm.py
"""

is_running = True
balance = 1000.00
menu = "1. Balance\n2. Deposit\n3. Withdraw\n4. Exit"
print("\n\t\tATM")

# I have made a variable for the ATM to indicate that it is on and running while in the following (while) loop below. It will also continue to run until its value has changed. The variable (balance) has a set value of 1000.00 dollars, indicating money in the bank account. I have created a menu of options the user can navigate. Finally, I made a simple print statement as a title to make the user aware of what they are interacting with.

while is_running:
    try:
        print(f"\n{menu}\n")
        user_request = int(input("\nPlease enter an option: "))
    except ValueError:
        print("\nPlease enter a numerical number.")
        continue

    # Above is the start of the program (while) loop and printing of the main menu along with the (user_request) asking for input from the user what they would like to do. This first (while) loop will have the program run continuously until the (is_running) variables value is changed. I have used a (try:except) block to make sure the user only inputs what is needed for the program to run as is designed. It catches alphabetical characters, spaces, and symbols that would cause errors and crash the program only allowing numerical numbers to be accepted.

    match user_request:
        case 1:
            print(f"\nYour current balance is ${balance:,.2f}")

        # I used (match:case) to "match" the value the user has input to the correct outputs according to the menu presented to the user. (case 1:) prints the output for menu option ("1. Balance") using an (f-string) along with (:,.2f) to ensure that the output presents the dollar amount fully with two decimal places.

        case 2:
            while True:
                try:
                    deposit = float(input("\nHow much would you like to deposit? "))
                    if deposit < 1:
                        print("\nInvalid amount, please try again.")
                    elif deposit > 1000000:
                        balance += deposit
                        print(f"\n${balance:,.2f}")
                        print("\nWhoa! I wish I was you!")
                        break
                    elif deposit > 0:
                        balance += deposit
                        print(f"\nYour new balance is ${balance:,.2f}")
                        break
                except ValueError:
                    print("\nInvalid number, please try again")
                    continue
        case 3:
            while True:
                try:
                    withdrawal = int(input("\nHow much would you like to withdraw? "))
                    if withdrawal < 0:
                        print(
                            "\nInvalid amount, you may only withdraw whole amounts, please try again."
                        )
                    elif withdrawal > 1000:
                        print("\nInsufficient funds")
                    elif withdrawal <= 1000:
                        balance -= withdrawal
                        print(f"\nYour new balance is ${balance:,.2f}")
                        break
                except ValueError:
                    print(
                        "\nInvalid number, you may only withdraw whole amounts, please try again."
                    )
                    continue

        # (case 2:) and (case 3:) uses its own (while) loop to ask the user for menu option ("2. Deposit")'s acceptable input while using (try:except) to make sure a numerical number is entered. I used (if/elif) statements with comparison operators to stop invalid amounts being accepted, along with math operators to output the new calculated balance with proper decimal presentation functions. (breaks) are coded in to exit the loop and return to the main menu loop for further tasks.

        case 4:
            print("\nGoodbye\n")
            is_running = False

        # In (case 4:) it performs option four by ending the main menu (while) loop via changing the (is_running) variables value to (False) and using a (print) statement to display "Goodbye" to the user ending their tasks and interactions with the program.

        case _:
            print("\nInvalid option, please try again.")

# (case _:) catches all other menu inputs made by the user that is not one of the options on the menu presented. This way the program runs without errors and continues to run until an acceptable input is entered.
