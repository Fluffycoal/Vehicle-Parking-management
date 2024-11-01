from abc import ABC, abstractmethod

# Abstract Base Class for Vehicle
class Vehicle(ABC):
    def __init__(self, license_plate, make, model, year, color, owner):
        self._license_plate = license_plate
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self.owner = owner  # Link to Owner

    @abstractmethod
    def vehicle_info(self):
        pass