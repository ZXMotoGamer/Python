"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

"""
Assignment: 8A
Date: 10/13/2026
File: data_mapping.py
"""


NATO_ALPHABET = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}
# Above, is a "dictionary" of the Nato Alphabet used as the database for this program.

MENU = """\n\t\tNato Encryption\n\n1. Enter English\n2. Enter Coded Word\n3. Quit\n"""
# Above, "MENU" serves as the title of the system along with the menu options displayed to the user.

print(f"\n{NATO_ALPHABET}")
# Above, this "print" statement displays the data in the "dictionary" for Master_Meri.

while True:  # This "while" loop keeps the program running until the user Quits.
    print(MENU)  # This "print" statement simply displays the menu to the user.
    try:
        menu_choice = int(
            input("\nEnter a menu option:  ")
        )  # This converts the user input to an integer option for the menu.
        match menu_choice:  # This "match:case" allows smooth menu navigation.
            case 1:
                while True:
                    try:
                        print('\nType "return" to go back to menu')
                        english_word = input("\nEnter a word:  ").strip().upper()
                        if english_word == "RETURN":
                            break
                        elif english_word != "":
                            pass
                        else:
                            print("\nInvalid entry, please enter a word.")
                            continue
                        for letter in english_word:
                            print(f"Code {letter}: {NATO_ALPHABET[letter]}")
                        break
                    except KeyError:
                        print("\nInvalid entry, please enter a word.")
                        continue
                    except Exception as e:
                        print(
                            f"\nUnexpected error: {e} has occurred, please try again."
                        )
                        continue
            # Above, "case 1:" uses a "for" loop to run through the letters of the word entered by the user and display the code words of the users entry. It uses "if/elif/else" statements to filter out unaccepted inputs and also allows the user a way to go back to the main menu. Finally "try:except" blocks to stop any possible crashes.

            case 2:
                while True:
                    try:
                        print('\nType "return" to go back to menu')
                        coded_word = (
                            input("\nEnter a coded word:  ").strip().capitalize()
                        )
                        if coded_word != "Return":
                            pass
                        else:
                            break
                        found = False
                        for key, value in NATO_ALPHABET.items():
                            if coded_word == value:
                                print(f"\nKey: {key}")
                                found = True
                                break
                        if not found:
                            print("\nSorry, word not in database.")
                            continue
                        break
                    except Exception as e:
                        print(
                            f"\nUnexpected error: {e} has occurred, please try again."
                        )
                        continue
            # Above, "case 2:" uses a different "for" loop to check if the users entered code word is in the database and if so displayed the "key" to the user. Like "case 1:" it uses "if/else" statements to filter out unaccepted inputs with a "try:except" block to stop any crashes

            case 3:
                print("\nGoodbye\n")
                break
            # Above, "case 3:" allows the user to quit the program.

            case _:
                print("\nInvalid option, please try again.")
                continue
            # Above, "case _:" catches any inputs that are not available in the menu.

    except ValueError:
        print("\nInvalid option, please try again.")
        continue
    except Exception as e:
        print(f"\nUnexpected error: {e} has occurred, please try again.")
        continue
    # This "try:except" blocks any invalid inputs to the menu that arn't accepted.
