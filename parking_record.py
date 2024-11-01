from datetime import datetime

# Class for ParkingRecord
class ParkingRecord:
    def __init__(self, vehicle, parking_spot):
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_time = datetime.now()
        self.exit_time = None

    def exit(self):
        self.exit_time = datetime.now()

    def record_info(self):
        exit_time = self.exit_time if self.exit_time else "Still parked"
        return f"Vehicle: {self.vehicle.vehicle_info()}, Spot: {self.parking_spot.spot_number}, Entry: {self.entry_time}, Exit: {exit_time}"