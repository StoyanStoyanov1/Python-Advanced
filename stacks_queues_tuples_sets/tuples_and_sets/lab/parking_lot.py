class ParkingLot:
    parking_lot = set()

    def __init__(self, current_cars):
        self.current_cars = current_cars
        self.parking_directions()

    def parking_directions(self):
        for direction in self.current_cars:
            command, car = direction.split(", ")
            if command == "IN":
                self.command_in(car)
            elif command == "OUT":
                self.command_out(car)

    def command_in(self, car):
        self.parking_lot.add(car)

    def command_out(self, car):
        self.parking_lot.remove(car)

    def __repr__(self):
        result = set()
        for car in self.parking_lot:
            result.add(car)

        if not result:
            return "Parking Lot is Empty"
        return "\n".join(result)



cars = [input() for _ in range(int(input()))]
print(ParkingLot(cars))
