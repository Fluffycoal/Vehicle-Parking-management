from owner import Owner
from car import Car
from parking_spot import ParkingSpot
from parking_record import ParkingRecord

class Main:
    def __init__(self):
        self.vehicles = []
        self.owners = []
        self.parking_spots = []
        self.parking_records = []

    def add_owner(self, first_name, last_name, phone_number, email):
        owner = Owner(first_name, last_name, phone_number, email)
        self.owners.append(owner)
        return owner

    def add_vehicle(self, license_plate, make, model, year, color, owner):
        vehicle = Car(license_plate, make, model, year, color, owner)
        self.vehicles.append(vehicle)

    def update_owner(self, old_owner, first_name, last_name, phone_number, email):
        old_owner._first_name = first_name
        old_owner._last_name = last_name
        old_owner._phone_number = phone_number
        old_owner._email = email

    def delete_owner(self, owner):
        self.owners.remove(owner)
        self.vehicles = [v for v in self.vehicles if v.owner != owner]  # Remove vehicles linked to this owner

    def update_vehicle(self, vehicle, license_plate, make, model, year, color):
        vehicle._license_plate = license_plate
        vehicle._make = make
        vehicle._model = model
        vehicle._year = year
        vehicle._color = color

    def delete_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def add_parking_spot(self, spot_number):
        spot = ParkingSpot(spot_number)
        self.parking_spots.append(spot)

    def park_vehicle(self, vehicle_license, spot_number):
        vehicle = next((v for v in self.vehicles if v._license_plate == vehicle_license), None)
        spot = next((s for s in self.parking_spots if s.spot_number == spot_number), None)

        if vehicle is None:
            return "Vehicle not found."
        if spot is None:
            return "Parking spot not found."
        if spot.is_occupied:
            return "Parking spot is already occupied."

        spot.is_occupied = True
        record = ParkingRecord(vehicle, spot)
        self.parking_records.append(record)
        return f"Vehicle {vehicle_license} parked in spot {spot_number}."

    def exit_vehicle(self, vehicle_license):
        record = next((r for r in self.parking_records if r.vehicle._license_plate == vehicle_license and r.exit_time is None), None)

        if record is None:
            return "Vehicle not found or not parked."

        record.exit()
        record.parking_spot.is_occupied = False
        return f"Vehicle {vehicle_license} exited from spot {record.parking_spot.spot_number}."

    def get_parking_records(self):
        return [record.record_info() for record in self.parking_records]

# Example usage
if __name__ == "__main__":
    parking_system = Main()

    # Adding owners
    owner1 = parking_system.add_owner("David", "Karanja", "705664332", "David@gmail.com")
    owner2 = parking_system.add_owner("Harun", "Abdi", "743526262", "Harun@gmail.com")

    # Adding vehicles
    parking_system.add_vehicle("KDM 546F", "Toyota", "Camry", 2020, "Blue", owner1)
    parking_system.add_vehicle("KDP 736Y", "Honda", "Civic", 2019, "Red", owner2)

    # Adding parking spots
    parking_system.add_parking_spot(1)
    parking_system.add_parking_spot(2)

    # Parking vehicles
    print(parking_system.park_vehicle("KDM 546F", 1))  # Should succeed
    print(parking_system.park_vehicle("KDP 736Y", 1))  # Should fail (spot already occupied)

    # Exiting vehicles
    print(parking_system.exit_vehicle("KDM 546F"))  # Should succeed
    print(parking_system.exit_vehicle("KDP 736Y"))  # Should fail (not parked)

    # Display parking records
    for record in parking_system.get_parking_records():
        print(record)