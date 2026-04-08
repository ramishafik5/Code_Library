#Question 2: Inheritance & Method Overriding

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        print(self.brand, self.model, "(",self.year,")")

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        
    def get_info(self):
        print(f"{self.brand} {self.model} ({self.year}) - {self.number_of_doors} doors")

class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type

    def get_info(self):
        print(f"{self.brand} {self.model} ({self.year}) - Type: {self.type}")

car = Car("Toyota", "Corolla", 2022, 4)
bike = Bike("Giant", "Escape 3", 2021, "Road")
car.get_info()
bike.get_info()