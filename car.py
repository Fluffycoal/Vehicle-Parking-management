from vehicle import Vehicle

# Class for Car, inheriting from Vehicle
class Car(Vehicle):
    def vehicle_info(self):
        return f"Car - {self._license_plate}, {self._make} {self._model}, {self._year}, {self._color}, Owner: {self.owner.owner_info()}"