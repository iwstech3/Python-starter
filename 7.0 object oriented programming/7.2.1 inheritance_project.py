
"""Problem: Vehicle Management System

You are tasked with creating a system to manage different types of vehicles in a transportation company. The system should be able to:

Calculate the fuel efficiency for each type of vehicle (e.g., car, truck, motorcycle).
Display details of each vehicle (e.g., make, model, fuel type).
Allow the company to add new vehicles and calculate total fuel usage over a specific period.
"""


class Vehicle:
    def __init__(self, make, model, fuel_type):
        self.make = make
        self.model = model
        self.fuel_type = fuel_type

    def display_info(self):
        return f"{self.make} {self.model} - Fuel Type: {self.fuel_type}"

    def calculate_fuel_efficiency(self, miles, fuel_consumed):
        """Calculate fuel efficiency in miles per gallon."""
        return miles / fuel_consumed

class Car(Vehicle):
    def __init__(self, make, model, fuel_type, num_doors):
        super().__init__(make, model, fuel_type)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()} - Doors: {self.num_doors}"

class Truck(Vehicle):
    def __init__(self, make, model, fuel_type, payload_capacity):
        super().__init__(make, model, fuel_type)
        self.payload_capacity = payload_capacity

    def display_info(self):
        return f"{super().display_info()} - Payload Capacity: {self.payload_capacity} kg"

class Motorcycle(Vehicle):
    def __init__(self, make, model, fuel_type, engine_capacity):
        super().__init__(make, model, fuel_type)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return f"{super().display_info()} - Engine Capacity: {self.engine_capacity} cc"

# Create instances of each type of vehicle
car = Car("Toyota", "Corolla", "Gasoline", 4)
truck = Truck("Volvo", "FH16", "Diesel", 18000)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", "Gasoline", 1200)

# Display vehicle info
print(car.display_info())
print(truck.display_info())
print(motorcycle.display_info())

# Calculate fuel efficiency for each vehicle (miles driven, fuel consumed)
print(f"Car Fuel Efficiency: {car.calculate_fuel_efficiency(400, 10)} mpg")
print(f"Truck Fuel Efficiency: {truck.calculate_fuel_efficiency(600, 50)} mpg")
print(f"Motorcycle Fuel Efficiency: {motorcycle.calculate_fuel_efficiency(250, 5)} mpg")
