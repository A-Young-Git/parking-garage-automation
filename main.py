from collections import namedtuple

"""
- The parking garage has 8 floors and 20 spaces per floor
- The customer is expected to go to the floor they are assigned 
- We start on the first floor, and work upwards. 
- As spaces open up on lower floors, direct new customers there. 
- Two functions, enter() and exit() will service these customers.
"""

garage = {"1": 20, "2": 20, "3": 20, "4": 20, "5": 20, "6": 20, "7": 20, "8": 20}

Ticket = namedtuple("Ticket", ["occupant_number", "garage_floor"])

active_tickets = []


def enter() -> str | None:
    for floor in garage:
        if garage[floor] > 0:
            garage[floor] -= 1
            return floor
    return None


def exit():
    while True:
        ticket_number = int(
            input("Please provide your ticket number and press 'Enter': ")
        )

        for ticket in active_tickets:
            if ticket_number == ticket[0]:
                active_tickets.remove(ticket)
                print("You are all set! Thanks for using T's Garage Services")
                return
            else:
                continue

        print(
            "Ticket number not found. Please check you entered it correctly and try again."
        )


if __name__ == "__main__":
    input("Welcome to T's Garage Services! Press 'Enter' to receive a ticket: ")

    floor = enter()

    if floor is not None:
        ticket = Ticket(occupant_number=1, garage_floor=floor)
        active_tickets.append(ticket)
        print(
            f"You have ticket number {ticket.occupant_number}. Please proceed to floor {ticket.garage_floor}"
        )
    else:
        print("Sorry. We are at full capacity. Please try again later.")

    exit()
