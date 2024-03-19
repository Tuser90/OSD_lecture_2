class Vehicle:
    def __init__(self, name, license_plate, color, fuel_type):
        self.name = name
        self.license_plate = license_plate
        self.color = color
        self.fuel_type = fuel_type

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_license_plate(self, license_plate):
        self.license_plate = license_plate

    def get_license_plate(self):
        return self.license_plate

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type

    def get_fuel_type(self):
        return self.fuel_type

# Create a new vehicle object
car = Vehicle("Honda Accord", "Accord123", "Blue", "Gasoline")

# Get vehicle attributes
print("Car Name:", car.get_name())
print("License Plate:", car.get_license_plate())
print("Color:", car.get_color())
print("Fuel Type:", car.get_fuel_type())

# Update vehicle attributes
car.set_color("Red")
car.set_fuel_type("Diesel")

# Get updated vehicle attributes
print("\nUpdated Color:", car.get_color())
print("Updated Fuel Type:", car.get_fuel_type())
