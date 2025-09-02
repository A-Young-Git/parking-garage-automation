from parking_garage import ParkingGarage

if __name__ == "__main__":
    print("Welcome to T's Garage Services!")
    input("Press 'Enter' to receive a ticket: ")

    parking_garage = ParkingGarage()
    ticket = parking_garage.enter()

    if ticket:
        print(
            f"You have ticket number {ticket.occupant_number}. "
            f"Please proceed to floor {ticket.garage_floor}"
        )
    else:
        print("Sorry. We are at full capacity. Please try again later.")
        exit()

    while True:
        try:
            ticket_input = int(input("Please provide your ticket number: "))
            if parking_garage.exit_garage(ticket_input):
                print("You are all set! Thanks for using T's Garage Services!")
                break
            else:
                print("Ticket number not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number")
