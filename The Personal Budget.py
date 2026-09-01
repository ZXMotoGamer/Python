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

budget_info = "Personal budget breakdown"
monthly_income = float(input("What is you're monthly income?: "))
# calculate net income as 80% of gross
rent = float(input("What is you're rent payment?: "))
# test for true/false function for utilities. (delete this before turning in)
utilities = float(input("What is you're utility payment?: "))
car_payment = float(input("What is you're car payment?: "))
phone = float(input("What is you're phone payment?: "))
groceries = float(input("What is you're cost for groceries?: "))
hobby = float(input("What is you're cost for entertainment?: "))

print(f"{budget_info}")

print("Bills........................................Cost")
print(f"Rent........................................{rent}")
