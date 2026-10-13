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
Date: 10//2026
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

MENU = "\n\t\tNato Encryption\n\n1. Enter English\n2. Enter Coded Word\n3. Quit\n"

while True:
    print(MENU)
    try:
        menu_choice = int(input("\nEnter a menu option:  "))
        match menu_choice:
            case 1:
                while True:
                    try:
                        english_word = input("\nEnter a word:  ").strip().upper()
                        # print(english_word)
                        # if english_word == " ":
                        #     print("\nMust enter a word")
                        #     continue
                        for letter in english_word:
                            if letter == " ":
                                print("\nMust enter a word")
                                continue
                            else:
                                print(NATO_ALPHABET[letter])
                            # for key, value in NATO_ALPHABET.items():
                            #     if letter in key:
                            #         print(value)
                            #         break
                            #     else:
                            #         print("\nInvalid word, please try again.")
                            #         continue
                        break
                    except KeyError:
                        print("\nUnexpected error, please try again.")
                        continue
            case 2:
                while True:
                    try:
                        coded_word = (
                            input("\nEnter a coded word:  ").strip().capitalize()
                        )
                        for key, value in NATO_ALPHABET.items():
                            if coded_word in value:
                                print(key)
                                break
                        break
                    except ValueError:
                        print("\nInvalid entry, please try again.")
                        continue
                    except KeyError:
                        print("\nUnexpected error, please try again.")
                        continue
            case 3:
                print("\nGoodbye\n")
                break
            case _:
                print("\nInvalid option, please try again.")
                continue
    except ValueError:
        print("\nInvalid option, please try again.")
    except Exception as e:
        print(f"\n{e}")
        continue
