"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

"""
Assignment 6A: Ticket Sales
Date 9/27/2026
File: tickets.py
"""

theater_seats = list(range(1, 21))
# Above is a variable for the list of seats in this program, done by using a list range from 1 to 20.

print("\n\t\tMovie Theater")
# Above si a title for the program running.

while True:
    print(f"\nSeats {theater_seats}")
    # Above (f-string) prints the (theater_seats) variable, along with a label in front of it indicating to the user that the list is for seats in the theater.
    try:
        if not theater_seats:
            print("\nSorry, seats are sold out!")
            break
            # Above (if not) to ensure that the user knows when all tickets have been sold out, along with a break to end the program due to the tickets being sold out.
        user_seat = int(input("\nWhat seat would you like? "))
        # Above (user_seat) gets the seat input from the user using an integer converting string via a printed question.
        if user_seat == 0:
            print("\nPerhaps next time!\n")
            break
            # Above (if) statement ensures that is the user does not want any seats to end the program if zero it entered.
        elif user_seat < 1 or user_seat > 20:
            print("\nSorry that is an invalid seat, please choose between seats 1-20.")
            continue
            # Above (elif) statement uses comparison operators to reject an input by the user that is less than 1 or greater than 20 when the option it 1-20.
        elif user_seat not in theater_seats:
            print("\nSorry that seat is taken, please choose another.\n")
            continue
            # Above (elif) statement uses (not in) to let the user know that the entered seat has been taken and to choose another.
        else:
            theater_seats.remove(user_seat)
            print("\nThank you for your purchase, enjoy the movie!\n")
            # Above (else) statement removes the entered input by the user from the list of seats. Along with a little message to confirm that the user got the seat.
    except ValueError:
        print("\nplease enter a seat number.")
        continue
        # Above (except) catches any input by the user that is not acceptable or that may cause an error.
