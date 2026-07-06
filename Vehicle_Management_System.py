class Vehicle:
    def get_data(self, Brand="", Model=""):
        self.Brand = Brand
        self.Model = Model

    def display(self):
        print(f"Brand = {self.Brand}")
        print(f"Model = {self.Model}")


class Car(Vehicle):
    def get_car_data(self, Fuel_type=""):
        self.Fuel_type = Fuel_type

    def display(self):
        print(f"Brand = {self.Brand}")
        print(f"Model = {self.Model}")
        print(f"Fuel Type = {self.Fuel_type}")


class Bike(Vehicle):
    def get_bike_data(self, Engine_capacity=""):
        self.Engine_capacity = Engine_capacity

    def display(self):
        print(f"Brand = {self.Brand}")
        print(f"Model = {self.Model}")
        print(f"Engine Capacity = {self.Engine_capacity}")


car1 = Car()
brand = input("Enter Car Brand: ")
model = input("Enter Car Model: ")
fuel = input("Enter Fuel Type: ")

car1.get_data(brand, model)
car1.get_car_data(fuel)

print("\nCar Details")
car1.display()


bike1 = Bike()
brand = input("Enter Bike Brand: ")
model = input("Enter Bike Model: ")
engine = input("Enter Engine Capacity: ")

bike1.get_data(brand, model)
bike1.get_bike_data(engine)

print("\nBike Details")
bike1.display()