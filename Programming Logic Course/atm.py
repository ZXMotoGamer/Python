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
while is_running:
    try:
        print(f"\n{menu}\n")
        user_request = int(input("\nPlease enter an option: "))
    except ValueError:
        print("\nPlease enter a numerical number.")
        continue
    match user_request:
        case 1:
            print(f"\nYour current balance is ${balance:,.2f}")
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
        case 4:
            print("\nGoodbye\n")
            is_running = False
        case _:
            print("\nInvalid option, please try again.")


# 1. need to add comments, also check registration assignment grading feedback on comments for better comment making.
# 2. need to confirm correct screenshot was taken.
# 3. start working on turning in registration.py_2.0
