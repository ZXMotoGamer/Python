"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float)(Rent, Utilities, etc.)
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

"""
Assignment 3A: Number Formatting & Math
9/2/2026
The Personal Budget
"""

budget_info = "Personal Budget Invoice"
bills = "Bills"
costs = "Costs"
# Variables above serve as titles of information.

gross_pay = float(input("\nWhat is you're monthly income?: "))
rent = float(input("\nWhat is you're monthly rent payment?: "))
utilities = float(input("\nWhat is you're monthly utility payment?: "))
car_payment = float(input("\nWhat is you're monthly vehicle payment?: "))
phone = float(input("\nWhat is you're monthly phone payment?: "))
groceries = float(input("\nWhat is you're monthly cost for groceries?: "))
hobby = float(input("\nWhat is you're monthly cost for entertainment?: "))
# Variables above ask for the required information to produce the budget.

tax = gross_pay * 0.2
net_pay = gross_pay - tax
total_expenses = rent + utilities + car_payment + phone + groceries + hobby
remaining_balance = net_pay - total_expenses
balance_percentage = total_expenses / net_pay
# Variables above perform the calculations for the budget output.

print(f"\n\n{budget_info:>35}")
print(f"\n{bills}{costs:>41}")
print("----------------------------------------------")
print(f"\nRent{rent:>42,.2f}")
print(f"\nUtilities{utilities:>37,.2f}")
print(f"\nVehicle{car_payment:>39,.2f}")
print(f"\nPhone{phone:>41,.2f}")
print(f"\nGroceries{groceries:>37,.2f}")
print(f"\nHobbies{hobby:>39,.2f}")
print("----------------------------------------------")
print(f"Total expenses{total_expenses:>32,.2f}")
print(f"Taxes withheld{tax:>32,.2f}")
print(f"Balance{remaining_balance:>39,.2f}")
print(f"Percentage spent{balance_percentage:>30.2%}\n")
# F-strings produce the output of the budget presented in a clean format.

# I wanted to simplify the code to line up all the output information nicely. Using manual spaces or dots to line up the information would result in misalignment if bigger numbers were given. I could not figure out how to input the $ symbol next to all the currency amounts, everything I attempted produced an error.
