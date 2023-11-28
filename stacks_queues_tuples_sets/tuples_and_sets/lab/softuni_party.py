class SoftUniParty:

    def __init__(self, reservation, arrival_guests):
        self.reservation = reservation
        self.arrival_guests = arrival_guests
        self.not_arrival_guests = self.not_arrival_guests()
        self.print_result()

    def not_arrival_guests(self):
        return set(self.reservation.difference(self.arrival_guests))

    def print_result(self):
        print(len(self.not_arrival_guests))

        for guest in sorted(self.not_arrival_guests):
            print(guest)


reservation = set(input() for _ in range(int(input())))
arrival_guests = set()

while True:
    guest = input()
    if guest == "END":
        break
    arrival_guests.add(guest)

SoftUniParty(reservation, arrival_guests)