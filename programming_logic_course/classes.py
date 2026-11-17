"""
-----------------------------------------------------------------------------------------------------------------------------
Assignment: 13A
Date: 11/16/2026
File: classes.py
-----------------------------------------------------------------------------------------------------------------------------
[ ] 1. Define classes using PascalCase and initialize attributes in "__init__" using underscores.
[ ] 2. Build getter and setter methods to access and modify attributes with validation.
[ ] 3. Make a summery method to output the complete state of the object and instantiate two objects to demonstrate the class.
[ ] 4. Include a checklist docstring header.
-----------------------------------------------------------------------------------------------------------------------------
"""

# I have had to put my comments in my own words of understanding.

SERVICES = ("Standard oil change", "Syn-blend oil change", "Full-syn oil change")
OIL_WEIGHT = ("10w30", "5w30", "5w20")
ADD_ONS = (
    "Air filter",
    "Cabin air filter",
    "Wiper blades",
    "Tire rotation",
    "Wheel alignment",
)
# Above constant are for demonstration use


class Ticket:  # CLASS Ticket is the factory
    def __init__(self, services, oil_weight, add_ons):
        self.__services = services
        self.__oil_weight = oil_weight
        self.__add_ons = add_ons

    # Class Ticket is the factory, __init__ is the method python uses to create objects, self is a parking spot for an object, and the parameters are arguments that have been passed to the class from (example) ticket1 from a main program. __services, __oil_weight, __add_ons are labels for the parking spots or (self) and the arguments are being assigned to those parking spots.

    def get_service(self):
        return self.__services

    def get_oil_weight(self):
        return self.__oil_weight

    def get_add_ons(self):
        return self.__add_ons

    # The getters are a way for a MAIN program to access data passed to the class that made it private via double underscores.

    def set_service(self, services):
        if services in SERVICES:
            self.__services = services

    def set_oil_weight(self, oil_weight):
        if oil_weight in OIL_WEIGHT:
            self.__oil_weight = oil_weight

    def set_add_ons(self, add_ons):
        if add_ons in ADD_ONS:
            self.__add_ons = add_ons

    # The setter methods are validating if the arguments are in the CONSTANTS and assigning them to the parking spots. These setter would need and "else" if the main program using them doesn't catch invalid options the user is entering.

    def get_summary(self):
        return f"\nTicket summary:\n{self.__services}\n{self.__oil_weight}\n{self.__add_ons}\n"


# get summary takes the arguments the class used to create an object and make an f-sting that can be displayed when called

ticket1 = Ticket("Standard oil change", "5w30", "Tire rotation")
ticket2 = Ticket("Full-syn oil change", "5w20", "Wheel alignment")

# the tickets 1 & 2 are variables that would be used in the main program to hold the object that the class has created. Thus rendering the variable as to being a complete bit of data that can be used to print out a work order for a mechanic.

print(ticket1.get_summary())
print(ticket2.get_summary())

# these display the objects within variables ticket1 and ticket2.
