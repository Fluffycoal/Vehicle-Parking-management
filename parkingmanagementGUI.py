import tkinter as tk
from tkinter import messagebox
from car import Car
from owner import Owner
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

    def add_vehicle(self, license_plate, make, model, year, color):
        vehicle = Car(license_plate, make, model, year, color)
        self.vehicles.append(vehicle)

    def add_parking_spot(self, spot_number):
        spot = ParkingSpot(spot_number)
        self.parking_spots.append(spot)

    def park_vehicle(self, vehicle_license, spot_number):
        vehicle = next((v for v in self.vehicles if v._license_plate == vehicle_license), None)
        spot = next((s for s in self.parking_spots if s.spot_number == spot_number), None)

        if vehicle is None or spot is None:
            return "Vehicle or parking spot not found."

        if spot.is_occupied:
            return "Parking spot is already occupied."

        spot.is_occupied = True
        record = ParkingRecord(vehicle, spot)
        self.parking_records.append(record)
        return f"Vehicle {vehicle_license} parked in spot {spot_number}."

    def exit_vehicle(self, vehicle_license):
        record = next((r for r in self.parking_records if r.vehicle._license_plate == vehicle_license and r.exit_time is None), None)

        if record is None:
            return "No active parking record found for this vehicle."

        record.exit()
        record.parking_spot.is_occupied = False
        return f"Vehicle {vehicle_license} has exited the parking spot."

    def show_parking_records(self):
        return [record.record_info() for record in self.parking_records]

class ParkingManagementGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Parking Management System")
        self.main_system = Main()

        # Create input fields for owner
        tk.Label(master, text="Owner First Name").grid(row=0)
        tk.Label(master, text="Owner Last Name").grid(row=1)
        tk.Label(master, text="Phone Number").grid(row=2)
        tk.Label(master, text="Email").grid(row=3)

        self.owner_first_name = tk.Entry(master)
        self.owner_last_name = tk.Entry(master)
        self.owner_phone = tk.Entry(master)
        self.owner_email = tk.Entry(master)

        self.owner_first_name.grid(row=0, column=1)
        self.owner_last_name.grid(row=1, column=1)
        self.owner_phone.grid(row=2, column=1)
        self.owner_email.grid(row=3, column=1)

        tk.Button(master, text='Add Owner', command=self.add_owner).grid(row=4, column=0, sticky=tk.W, pady=4)

        # Create input fields for vehicle
        tk.Label(master, text="License Plate").grid(row=5)
        tk.Label(master, text="Make").grid(row=6)
        tk.Label(master, text="Model").grid(row=7)
        tk.Label(master, text="Year").grid(row=8)
        tk.Label(master, text="Color").grid(row=9)

        self.vehicle_license = tk.Entry(master)
        self.vehicle_make = tk.Entry(master)
        self.vehicle_model = tk.Entry(master)
        self.vehicle_year = tk.Entry(master)
        self.vehicle_color = tk.Entry(master)

        self.vehicle_license.grid(row=5, column=1)
        self.vehicle_make.grid(row=6, column=1)
        self.vehicle_model.grid(row=7, column=1)
        self.vehicle_year.grid(row=8, column=1)
        self.vehicle_color.grid(row=9, column=1)

        tk.Button(master, text='Add Vehicle', command=self.add_vehicle).grid(row=10, column=0, sticky=tk.W, pady=4)

        # Create input fields for parking spot
        tk.Label(master, text="Parking Spot Number").grid(row=11)
        self.parking_spot_number = tk.Entry(master)
        self.parking_spot_number.grid(row=11, column=1)

        tk.Button(master, text='Add Parking Spot', command=self.add_parking_spot).grid(row=12, column=0, sticky=tk.W, pady=4)

        # Create input fields for parking vehicle
        tk.Label(master, text="Vehicle License Plate").grid(row=13)
        tk.Label(master, text="Parking Spot Number").grid(row=14)

        self.parking_vehicle_license = tk.Entry(master)
        self.parking_spot_number = tk.Entry(master)

        self.parking_vehicle_license.grid(row=13, column=1)
        self.parking_spot_number.grid(row=14, column=1)

        tk.Button(master, text='Park Vehicle', command=self.park_vehicle).grid(row=15, column=0, sticky=tk.W, pady=4)

        # Create input fields for exiting vehicle
        tk.Label(master, text="Vehicle License Plate").grid(row=16)
        self.exiting_vehicle_license = tk.Entry(master)
        self.exiting_vehicle_license.grid(row=16, column=1)

        tk.Button(master, text='Exit Vehicle', command=self.exit_vehicle).grid(row=17, column=0, sticky=tk.W, pady=4)

        # Create button to show parking records
        tk.Button(master, text='Show Parking Records', command=self.show_parking_records).grid(row=18, column=0, sticky=tk.W, pady=4)

    def add_owner(self):
        first_name = self.owner_first_name.get()
        last_name = self.owner_last_name.get()
        phone_number = self.owner_phone.get()
        email = self.owner_email.get()

        self.main_system.add_owner(first_name, last_name, phone_number, email)
        messagebox.showinfo("Success", "Owner added successfully.")

    def add_vehicle(self):
        license_plate = self.vehicle_license.get()
        make = self.vehicle_make.get()
        model = self.vehicle_model.get()
        year = self.vehicle_year.get()
        color = self.vehicle_color.get()

        self.main_system.add_vehicle(license_plate, make, model, year, color)
        messagebox.showinfo("Success", "Vehicle added successfully.")

    def add_parking_spot(self):
        spot_number = int(self.parking_spot_number.get())
        self.main_system.add_parking_spot(spot_number)
        messagebox.showinfo("Success", "Parking spot added successfully.")

    def park_vehicle(self):
        vehicle_license = self.parking_vehicle_license.get()
        spot_number = int(self.parking_spot_number.get())
        result = self.main_system.park_vehicle(vehicle_license, spot_number)
        messagebox.showinfo("Result", result)

    def exit_vehicle(self):
        vehicle_license = self.exiting_vehicle_license.get()
        result = self.main_system.exit_vehicle(vehicle_license)
        messagebox.showinfo("Result", result)

    def show_parking_records(self):
        records = self.main_system.show_parking_records()
        messagebox.showinfo("Parking Records", "\n".join(records))

root = tk.Tk()
my_gui = ParkingManagementGUI(root)
root.mainloop()