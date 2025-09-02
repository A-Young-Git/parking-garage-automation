import itertools
from dataclasses import dataclass

"""
This ParkingGarage class initializes with an 8 floor and 20 space 
per floor capacity. It holds an enter() and exit_garage() method for customers
entering and exiting the ParkingGarage. Tickets are added/removed 
via an active tickets array. 
"""


@dataclass
class Ticket:
    occupant_number: int
    garage_floor: str


class ParkingGarage:
    def __init__(self) -> None:
        self.active_tickets = []
        self.capacity = {str(i): 20 for i in range(1, 9)}
        self.ticket_counter = itertools.count(1)

    def enter(self) -> Ticket | None:
        for floor, spots in self.capacity.items():
            if spots > 0:
                self.capacity[floor] -= 1
                ticket = Ticket(next(self.ticket_counter), floor)
                self.active_tickets.append(ticket)
                return ticket
        return None

    def exit_garage(self, ticket_number: int) -> bool:
        for ticket in self.active_tickets:
            if ticket_number == ticket.occupant_number:
                self.active_tickets.remove(ticket)
                self.capacity[ticket.garage_floor] += 1
                return True

        return False
