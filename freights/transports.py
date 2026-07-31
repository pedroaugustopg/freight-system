from abc import ABC, abstractmethod


class Transport(ABC):

    def __init__(self, distance):
        self.distance = distance
        self.freight = 0

    @abstractmethod
    def freight_calc(self):
        pass

class Motorcycle (Transport):
    freight_factor = 0.50

    def __init__(self, distance):
        super().__init__(distance)

    def freight_calc(self):
        self.freight = self.distance * Motorcycle.freight_factor
        return f"R$ {self.freight:.2f}"

class Truck(Transport):
    freight_factor = 1.20

    def __init__(self, distance):
        super().__init__(distance)

    def freight_calc(self):
        if self.distance < 50:
            self.freight = 0
            return "For trucks, the minimum radius for freight deliveries is 50 km."
        else:
            self.freight = self.distance * Truck.freight_factor
            return f"R$ {self.freight:.2f}"

class Drone (Transport):
    freight_factor = 9.50

    def __init__(self, distance):
        super().__init__(distance)

    def freight_calc(self):
        if self.distance < 10:
            self.freight = 0
            return "For drones, the minimum radius for freight deliveries is 10 km."
        else:
            self.freight = self.distance * Drone.freight_factor
            return f"R$ {self.freight:.2f}"