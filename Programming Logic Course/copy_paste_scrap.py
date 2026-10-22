JAGEX = "Runescape Accounts"

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


# data_maapper.py Scrap:
while True:
    try:
        user_input = input("\nEnter a word: ").strip().upper()
        if user_input == "QUIT":
            print("\nGoodbye\n")
            break
        for letter in user_input:
            for key, value in NATO_ALPHABET.items():
                if letter == key:
                    print(value)
                    continue
    except Exception as e:
        print(f"{e}")
        continue
# --------------------------------------------------------------


# sample:
def validate_age(age):
    # Example function that checks if the input meets specific criteria
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return True


# --- Looping the Input Statement ---
while True:
    try:
        # 1. Get input from the user
        user_input = int(input("Please enter your age: "))

        # 2. Pass to the function / validate
        validate_age(user_input)

        # 3. If valid, break out of the loop
        print(f"Success! Your age is {user_input}.")
        break

    except ValueError as e:
        # Catches non-integers or custom ValueError exceptions raised by the function
        print(f"Invalid input: {e}. Please try again.\n")
