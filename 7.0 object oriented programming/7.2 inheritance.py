

class Vehicle:
  
    
    def __init__(self, make, model):
      
        self.make = make    # Instance attribute for manufacturer
        self.model = model  # Instance attribute for model name
        
    def display_info(self):
       
        return f"{self.make} {self.model}"


class Car(Vehicle):

    def __init__(self, make, model, doors):
       
        # Call parent's constructor first
        super().__init__(make, model)
        # Add Car-specific attributes
        self.doors = doors
    
    def display_info(self):
    
    
        return f"{super().display_info()} - {self.doors} doors"


class ElectricCar(Car):
  
    
    def __init__(self, make, model, doors, battery_capacity, range):
        super().__init__(make, model, doors)
        self.battery_capacity = battery_capacity
        self.range = range
        self._charge_level = 100  # Protected attribute (single underscore)
        
    def display_info(self):
        """Demonstrates further method overriding"""
        return (f"{super().display_info()} - "
                f"Battery: {self.battery_capacity}kWh, "
                f"Range: {self.range}mi")
    
    @property  # Decorator for getter
    def charge_level(self):
        """Demonstrates property decorator for getter"""
        return self._charge_level
    
    @charge_level.setter  # Decorator for setter
    def charge_level(self, value):
        """Demonstrates property setter with validation"""
        if 0 <= value <= 100:
            self._charge_level = value
        else:
            raise ValueError("Charge level must be between 0 and 100")



def demonstrate_inheritance():
    # Create instances of each class
    generic_vehicle = Vehicle("Generic", "Vehicle")
    regular_car = Car("Toyota", "Camry", 4)
    tesla = ElectricCar("Tesla", "Model 3", 4, 75, 310)
    
    # Demonstrate inheritance hierarchy
    print("Basic Vehicle:", generic_vehicle.display_info())
    print("Regular Car:", regular_car.display_info())
    print("Electric Car:", tesla.display_info())
    
    # Demonstrate property usage
    print(f"Tesla charge level: {tesla.charge_level}%")
    tesla.charge_level = 80  # Using the setter
    print(f"Updated charge level: {tesla.charge_level}%")
    
    # Demonstrate isinstance() checks
    print(f"\nInheritance checks:")
    print(f"Is tesla a Vehicle? {isinstance(tesla, Vehicle)}")
    print(f"Is tesla a Car? {isinstance(tesla, Car)}")
    print(f"Is tesla an ElectricCar? {isinstance(tesla, ElectricCar)}")

# Run demonstrations
if __name__ == "__main__":
    demonstrate_inheritance()